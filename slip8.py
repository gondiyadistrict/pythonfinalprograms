#Q.1

# Sample set
my_set = {1, 2, 3, 4, 5}

# Calculate the average
average = sum(my_set) / len(my_set)

# Print the average
print(f"Average of elements in the set: {average}")

#Q.2
# Sample dictionaries
dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

# Check for common keys with the same values
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        print(f"{key}: {dict1[key]} is present in both dict1 and dict2")

#Q.3
# Sample list
numbers = (8, 2, 3, -1, 7)

# Initialize product as 1
product = 1

# Multiply all numbers in the list
for num in numbers:
    product *= num

# Print the result
print(f"Product of all numbers in the list: {product}")

