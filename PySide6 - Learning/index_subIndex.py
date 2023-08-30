import csv

# Initialize an empty list to store the values from the first column
first_column_values = []

# Open the CSV file for reading
with open('v3.0.0 - Akash_m2 (1) (2).csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        first_column_values.append(row[0])

# Print the list of values from the first column
# print(first_column_values)
first_column_values = first_column_values[1:]
print(first_column_values)

int_addresses = [int(hex_address, 16) >> 8 for hex_address in first_column_values]
print(int_addresses)
# shifted_hex_addresses = [hex(address) for address in int_addresses]
# print(shifted_hex_addresses)
