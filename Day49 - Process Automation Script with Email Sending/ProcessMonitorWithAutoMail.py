import urllib
import urllib.request
import urllib.error
import time
import os
import psutil
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected():
    try:
        urllib.request.Request("http://216.58.192.142")
        return True
    except urllib.error as err:
        return False


def MailSender(filename, time):
    try:
        fromAddress = "abc@gmail.com"
        toAddress = "xyz@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = fromAddress
        msg['To'] = toAddress

        mailBody = """
		Hello %s,
		Welcome to my automation script.
		PFA containing Log of running processes.
		Log file created at : %s

		This is auto generetated email.

	    Thanks,
		""" % (toAddress, time)
        mailSubject = """
		Process Monitor with Auto Send Mail (Log file created at : %s) 
		""" % (time)

        msg['Subject'] = mailSubject
        msg.attach(MIMEText(mailBody, 'plain'))
        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename = %s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromAddress, "MY_PASSWORD")
        text = msg.as_string()
        s.sendmail(fromAddress, toAddress, text)
        s.quit()

        print("Lof file sent successfully through mail.")

    except Exception as err:
        print("Unable to send file", err)


def ProcessLog(log_dir="MyLogs"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir, "MarvellousLog%s.log" % (time.strftime('%Y-%m-%d_%H-%M-%S')))
    # log_path = os.path.join(log_dir, "MarvellousLog%s.log" % (time.ctime()))
    with open(log_path, "w") as file:
        file.write(separator + "\n")
        file.write("Marvellous Infosystems Process Logger : " + time.ctime() + "\n")
        file.write(separator + "\n")
        file.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        file.write("%s\n" % element)

    print("Log file is successfully generated at location : %s" % (log_path))

    connected = is_connected()

    if connected:
        starttime = time.time()
        MailSender(log_path, time.ctime())
        endtime = time.time()

        print("Took %s seconds to send mail : " % (endtime - starttime))

    else:
        print("No Internet Connection.")


def main():
    print("App name : ", argv[0])

    if len(argv) != 2:
        print("Error : invalid no. of arguments.")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used for log records of running processes.")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : App_Name Time_Interval_in_Minutes")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as err:
        print("Error : Invalid input", err)


if __name__ == "__main__":
    main()
