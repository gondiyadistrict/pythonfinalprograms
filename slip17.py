#Q.1
# Accept input from the user
user_input = input("Enter a string: ")

# Ask user whether to convert to uppercase or lowercase
choice = input("Convert to (U)ppercase or (L)owercase: ").strip().upper()

if choice == 'U':
    # Convert string to uppercase
    print(f"Converted to Uppercase: {user_input.upper()}")
elif choice == 'L':
    # Convert string to lowercase
    print(f"Converted to Lowercase: {user_input.lower()}")
else:
    print("Invalid choice! Please select 'U' for Uppercase or 'L' for Lowercase.")


#Q.2
# Accept the integer input from the user
n = int(input("Enter a number: "))

print(f"Prime numbers up to {n} are:")

# Loop through all numbers from 2 to n
for num in range(2, n + 1):
    # Check if the current number is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")


#Q.3

# Accept input for number of rows in Floyd's triangle
n = int(input("Enter the number of rows for Floyd's triangle: "))

num = 1
# Loop through rows
for i in range(1, n + 1):
    # Loop through each column in the current row
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
