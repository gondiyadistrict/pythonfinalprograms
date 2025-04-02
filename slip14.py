#Q.1
# Accept n numbers from the user
n = int(input("Enter the number of elements in the tuple: "))

# Create a list to store the elements
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Create a tuple from the list
num_tuple = tuple(numbers)

# Calculate the maximum, minimum, and sum
max_value = max(num_tuple)
min_value = min(num_tuple)
sum_value = sum(num_tuple)

# Print the results
print(f"Tuple: {num_tuple}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Sum of elements: {sum_value}")


#Q.2
# Accept input from the user
n = int(input("Enter a number n: "))
print(f"Prime numbers till {n} are:")

# Iterate through numbers from 2 to n
for num in range(2, n + 1):
    # Check if the number is prime
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Check divisibility till square root of num
        if num % i == 0:
            is_prime = False
            break
    # If the number is prime, print it
    if is_prime:
        print(num, end=" ")

#Q.3
# Accept input expression from the user
expression = input("Enter a string of parentheses: ")

# Dictionary to map open and close parentheses
pairs = {'(': ')', '{': '}', '[': ']'}

# Stack to keep track of opening parentheses
stack = []

# Variable to keep track of validity
is_valid = True

# Iterate through each character in the expression
for char in expression:
    # If it's an opening parenthesis, push it to the stack
    if char in pairs:
        stack.append(char)
    # If it's a closing parenthesis, check for validity
    elif char in pairs.values():
        if not stack or pairs[stack.pop()] != char:
            is_valid = False
            break

# The expression is valid if the stack is empty at the end
if is_valid and not stack:
    print("The expression has valid parentheses.")
else:
    print("The expression has invalid parentheses.")
