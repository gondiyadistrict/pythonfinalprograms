#Q.1
Tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

front = Tuple[4]
last = Tuple[-5]

print("5th element from front:", front)
print("5th element from last:", last)

#Q.2
dic1={'a':100,'b':200,'c':300}
dic2={'a':300,'b':200,'d':400}
dic3=dic1.copy()
for key, value in dic2.items():
    if key in dic3:
        dic3[key]+=value
    else:
        dic3[key]=value
for key,value in dic3.items():
    print(f'{key}:{value}')

#Q.3
    #symmetric diff
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
    # intersection of sets.

set1={1,2,3,4,5}
set2={4,5, 6,7,8}

print(set1|set2)
print(set1 & set2)

# maximum and the minimum value in a set.
set = {10, 20, 30, 40, 50}

max_value = max(set)
min_value = min(set)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
