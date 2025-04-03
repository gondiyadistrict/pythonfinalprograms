#Q.1
# Anonymous function to calculate the area of a square
side_length = float(input("Enter the side length of the square: "))

# Lambda function to calculate area
area = (lambda side: side * side)(side_length)

print(f"The area of the square is: {area}")


#Q.2
# Accept n elements in a set
n = int(input("Enter the number of elements in the set: "))
elements = set()

# Accept n elements from the user
for _ in range(n):
    element = int(input("Enter an element: "))
    elements.add(element)

# Calculate length of the set
length = 0
for _ in elements:
    length += 1

# Calculate maximum value
max_value = None
for element in elements:
    if max_value is None or element > max_value:
        max_value = element

# Calculate minimum value
min_value = None
for element in elements:
    if min_value is None or element < min_value:
        min_value = element

# Calculate sum of the values
total_sum = 0
for element in elements:
    total_sum += element

# Display the results
print(f"Length of the set: {length}")
print(f"Maximum value in the set: {max_value}")
print(f"Minimum value in the set: {min_value}")
print(f"Sum of values in the set: {total_sum}")



#Q.3
# Function to count frequency of characters
def count_frequency(string):
    frequency = {}
    
    # Iterate through each character in the string
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

# Accept input from the user
input_string = input("Enter a string: ")

# Call the function and display the frequency of characters
char_frequency = count_frequency(input_string)
print("Character frequency:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
