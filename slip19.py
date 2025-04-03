#Q.1
# Sample list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the sum of numbers in the list
total_sum = sum(numbers)

# Calculate the number of elements in the list
length = len(numbers)

# Calculate the average
average = total_sum / length

# Display the result
print(f"The average of the numbers in the list is: {average}")



#Q.2
# Function to get a string made of first 2 and last 2 chars
def get_first_and_last_2_chars(string):
    if len(string) < 2:
        return ""  # Return empty string if length is less than 2
    else:
        return string[:2] + string[-2:]  # Concatenate the first 2 and last 2 chars

# Sample test cases
sample_string1 = "General12"
sample_string2 = "Ka"
sample_string3 = " K"

# Call the function and print the results
print(f"Result for '{sample_string1}': {get_first_and_last_2_chars(sample_string1)}")
print(f"Result for '{sample_string2}': {get_first_and_last_2_chars(sample_string2)}")
print(f"Result for '{sample_string3}': {get_first_and_last_2_chars(sample_string3)}")




#Q.3
# Number of rows
n = 4

# Loop to print the pattern
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row
