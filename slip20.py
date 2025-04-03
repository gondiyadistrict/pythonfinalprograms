#Q.1
# Input for side length of the square
side_length = float(input("Enter the side length of the square: "))

# Anonymous function to calculate area
area = (lambda side: side * side)(side_length)

print(f"The area of the square is: {area}")



#Q.2

# Accept the number from the user
n = int(input("Enter a number: "))

# Initialize sum variable
sum_of_digits = 0

# Loop to extract each digit and add to the sum
while n > 0:
    sum_of_digits += n % 10  # Get the last digit
    n = n // 10  # Remove the last digit

# Display the sum of digits
print(f"The sum of the digits is: {sum_of_digits}")

#Q.3
import string

# Accept input string from the user
input_string = input("Enter a string: ")

# Remove punctuation and special symbols using a list comprehension
cleaned_string = ''.join(char for char in input_string if char not in string.punctuation)

# Display the cleaned string
print(f"The string without special characters is: {cleaned_string}")
