#Q.1
# Input the number of elements in the tuple
n = int(input("Enter the number of elements in the tuple: "))

# Input n elements and create a tuple
numbers = tuple(int(input(f"Enter element {i+1}: ")) for i in range(n))

# Calculate the mid-point to divide the tuple into two halves
mid = n // 2

# Print the first half of the tuple
print("First half of the tuple:")
print(numbers[:mid])

# Print the second half of the tuple
print("Second half of the tuple:")
print(numbers[mid:])


#Q.2
# Input the number of terms to be printed in the Fibonacci series
num_terms = int(input("Enter the number of terms for Fibonacci series: "))

# Initialize the first two terms
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci Series:")
for _ in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b  # Update a and b to the next two numbers


#Q.3

# Input the number of elements in the dictionary
n = int(input("Enter the number of key-value pairs: "))

# Create an empty dictionary
my_dict = {}

# Input n key-value pairs
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

# Input the key to check
key_to_check = input("Enter the key to check if it exists in the dictionary: ")

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists. Replacing value.")
    # Replace the value for the given key
    new_value = input(f"Enter new value for key '{key_to_check}': ")
    my_dict[key_to_check] = new_value
else:
    print(f"Key '{key_to_check}' does not exist.")

# Print the updated dictionary
print("Updated Dictionary:")
print(my_dict)
