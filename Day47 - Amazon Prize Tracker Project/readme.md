# Amazon Price Alert 
This code checks the price of an Amazon product and sends an email if the price drops below a certain threshold.

* To use the code.
1) Set the email and password variables to your email address and password.
2) Set the amazon_product_website variable to the URL of the Amazon product page.
3) Set the my_desired_price variable to the desired price of the product.

To run the code
Open a terminal window.
Navigate to the directory where the code is located.
Execute the following command:
**python main.py**

The code will then check the price of the product and send an email if the price drops below the desired price.

Example
The following example shows how to set the variables and run the code:

email = "your_email_address"
password = "your_email_password"
amazon_product_website = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
my_desired_price = 200


In this example, the code will check the price of the product at the URL https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1. If the price of the product drops below 200, the code will send an email to your_email_address.