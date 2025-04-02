#Q.1
#Write a Python program to find the repeated items of a tuple.
from collections import Counter

# Sample tuple
my_tuple = (1, 2, 3, 4, 5, 2, 3, 6, 7, 2)

# Count the occurrences of each element in the tuple
count = Counter(my_tuple)

# Print the repeated items
print("Repeated items in the tuple:")
for item, freq in count.items():
    if freq > 1:
        print(f"Item: {item}, Repeated {freq} times")

#Q.2
        # Define two dictionaries
dict_x = {'key1': 1, 'key2': 3, 'key3': 2}
dict_y = {'key1': 1, 'key2': 2}

# Compare values for common keys
for key in dict_x:
    if key in dict_y and dict_x[key] == dict_y[key]:
        print(f"{key}: {dict_x[key]} is present in both x and y")

#Q.3

# Create a set with 3 weekdays
weekdays = {"Monday", "Tuesday", "Wednesday"}

# Add a single element to the set
weekdays.add("Thursday")

# Print the set after adding one element
print("After adding one day:", weekdays)

# Add multiple elements to the set
weekdays.update({"Friday", "Saturday"})

# Print the set after adding multiple elements
print("After adding multiple days:", weekdays)

