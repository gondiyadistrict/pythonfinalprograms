#Q.1
# Accept a string from the user
input_string = input("Enter a string: ")

# Initialize a counter
length = 0

# Loop through the string and count characters
for char in input_string:
    length += 1

# Print the length of the string
print(f"The length of the string is: {length}")


#Q.2
# Function to remove characters with odd index values
def remove_odd_index_chars(input_string):
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 0:  # Keep characters with even indices
            result += input_string[i]
    return result

# Accept a string from the user
input_string = input("Enter a string: ")

# Call the function and print the result
modified_string = remove_odd_index_chars(input_string)
print(f"String after removing characters with odd indices: {modified_string}")

#Q.3
# Accept n numbers from the user
n = int(input("Enter the number of elements in the list: "))
numbers = []

for _ in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)

# Remove duplicates by converting the list to a set and then back to a list
numbers = list(set(numbers))

# Print the list with duplicates removed
print(f"List after removing duplicates: {numbers}")
