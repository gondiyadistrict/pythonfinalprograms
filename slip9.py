#Q.1
# Sample tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Create a new tuple by concatenating the two tuples
new_tuple = tuple1 + tuple2

# Print the new tuple
print(f"New tuple: {new_tuple}")


#Q.2
# Sample dictionary
my_dict = {'key1': 5, 'key2': 1, 'key3': 8, 'key4': 3}

# Sort dictionary by value in ascending order
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort dictionary by value in descending order
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print sorted dictionaries
print(f"Sorted by value (ascending): {ascending}")
print(f"Sorted by value (descending): {descending}")


#Q.3
# Sample sentence
sentence = "this is a test sentence and this is a test"

# Split the sentence into words
words = sentence.split()

# Initialize an empty dictionary to count occurrences
word_count = {}

# Count the occurrences of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Print the word count
print("Word count:", word_count)

