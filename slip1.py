#Q.1

def is_in_range(number, start, end):
    return start <= number <= end
print(is_in_range(5,1,10))
print(is_in_range(15,1,10))

#Q.2

# union of sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2 

print("Union of the sets:", union_set)

#intersection of sets.

set1={1,2,3,4,5}
set2={4,5, 6,7,8}

print(set1|set2)
print(set1 & set2)

# symmetric difference

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

#Q.3

n= int(input("enter a number:"))
d=dict()
for x in range(10,15):
    d[x]=x*x
print(d)

