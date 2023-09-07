import matplotlib.pyplot as plt
import csv

# Read the CSV data
with open('Y35.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Ignore the first row
    data = list(reader)

# Extract the x and y data
x_data = [float(row[0].replace('\t', '').replace(' ', '')) for row in data]
print(x_data)
y_data = [float(row[1]) for row in data]

# Plot the data
plt.plot(x_data, y_data)

# Add labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph of csv data')

# Show the plot
plt.show()
