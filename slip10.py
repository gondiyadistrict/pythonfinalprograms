#Q.1
# Anonymous function to calculate the area of a square
area_of_square = lambda side: side * side

# Test the function
side_length = 5
print(f"Area of square with side {side_length}: {area_of_square(side_length)}")


#Q.2
# Sample string
sample_string = "Hello all"

# Create a dictionary to store character frequencies
char_count = {}

# Loop through each character in the string
for char in sample_string:
    if char != ' ':  # Skip spaces
        char_count[char] = char_count.get(char, 0) + 1

# Print the dictionary
print(char_count)


#Q.3
# Function to count the frequency of each character
def count_char_frequency(input_string):
    # Dictionary to store the character frequencies
    freq_dict = {}
    
    # Loop through each character in the string
    for char in input_string:
        if char != ' ':  # Skip spaces
            freq_dict[char] = freq_dict.get(char, 0) + 1
    
    return freq_dict

# Sample string
sample_string = "Hello all"

# Call the function and print the result
result = count_char_frequency(sample_string)
print(result)
