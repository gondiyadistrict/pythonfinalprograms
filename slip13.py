#Q.1
# Accept the number of terms for the Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update a and b to the next terms

#Q.2

# Accept a string from the user
input_string = input("Enter a string: ")

# Get the first character of the string
first_char = input_string[0]

# Replace all occurrences of the first character (except the first one) with '$'
modified_string = first_char + input_string[1:].replace(first_char, '$')

# Print the modified string
print("Modified string:", modified_string)


#Q.3
# Accept the value of n
n = int(input("Enter the value of n: "))

# Generate and print the dictionary
square_dict = {x: x*x for x in range(1, n+1)}

# Print the dictionary
print("Generated Dictionary:", square_dict)
