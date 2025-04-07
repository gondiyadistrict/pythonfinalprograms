#question 1
my_tuple = (10, 20, 30, 40)

# Unpacking the tuple into variables
a, b, c, d = my_tuple

# Displaying the unpacked values
print("Unpacked values:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:",d)

#question 2
elements=[]
for i in range(6):
    num = int(input(f"Enter element {i + 1}: "))
    elements.append(num)
if len(elements)!=len(set(elements)):
        print("duplicate")
else:
        print("all unique")

#question 3
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
