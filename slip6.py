#Q.1
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
diff=set()
for item in set1:
    if item not in set2:
        diff.add(item)
    print("set diff:",diff)
    symmetric_diff=set()
    for item in set1:
        if item not in set2:
            symmetric_diff.add(item)
    for item in set2:
        if item not in set1:
            symmetric_diff.add(item)
    print("symmetric difference:",symmetric_diff)

#Q.2
import itertools

# Sample dictionary
data = {'1': ['a', 'b'], '2': ['c', 'd']}

# Generate combinations
for combo in itertools.product(*data.values()):
    print(''.join(combo))
# 


#Q.3
data_tuple = ('a', 'b', 'c', 'a', 'a', 'd', 'b', 'a', 'c')

# Count and display elements appearing more than twice
for item in set(data_tuple):
    if data_tuple.count(item) > 2:
        print(f"{item} appears more than 2 times")
