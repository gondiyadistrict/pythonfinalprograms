#Q.1
#Sort the tuple - Tuple-(2, 4, 6, 1, 4, 7.8, 2.7)
'''
Tuple = (2, 4, 6, 1, 4, 7.8, 2.7)
sorted_tuple = tuple(sorted(Tuple))
print("Sorted tuple:", sorted_tuple)
'''
#Q.2

def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)
print(sum_recursive(10))

#Q.3

#1. Write a Python program to create a dictionary from two lists without losing duplicate values.

#Sample lists: ['Class-V', 'Class-VI', 'Class-VII','Class-VIII'], [1. 2. 2, 31

#Expected Output: defaultdict(<class 'set'>, "Class-VII (2), 'Class-VI: (2), 'Class-VII (3), 'Class-V: {1}})
'''
from collections import defaultdict
class_list = ['class-v','class-vi','class-vii','class-viii']
id_list=[1,2,2,3]
temp= defaultdict(set)
for c, i in zip(class_list, id_list):
    temp [c].add(i)
print(temp)
'''
