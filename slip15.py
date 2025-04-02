#Q.1
# Accept input string from the user
string = input("Enter a string: ")

# Remove spaces and convert the string to lowercase for case-insensitive comparison
cleaned_string = ''.join(string.split()).lower()

# Check if the cleaned string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#Q.2
# Function for sequential search in a sorted list
def sequential_search(sorted_list, item):
    for index in range(len(sorted_list)):
        if sorted_list[index] == item:
            return index  # Return the index of the item if found
    return -1  # Return -1 if item is not found

# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]  # A sorted list
item = int(input("Enter the item to search for: "))

result = sequential_search(sorted_list, item)

if result != -1:
    print(f"Item found at index: {result}")
else:
    print("Item not found in the list.")

#Q.3

# Accept the number from the user
number = int(input("Enter a number: "))

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Iterate through each digit of the number
while number > 0:
    # Extract the last digit of the number
    digit = number % 10
    sum_of_digits += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit

# Print the sum of digits
print(f"The sum of the digits is: {sum_of_digits}")
