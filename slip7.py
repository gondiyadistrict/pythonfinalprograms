#Q.1
# Write a Python program to find maximum and the minimum value in a set.
set = {10, 20, 30, 40, 50}

max_value = max(set)
min_value = min(set)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

#Q.2
#Write a Python script to generate and print a dictionary that contains a number (Between

#1 and n) in the form (x, x*x).

#Sample Dictionary (n=5)

#Expected Output {1 1,2:4, 3:9, 4: 16,5:25)
'''
n= int(input("enter a number:"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
'''

#Q.3
#Write a Python program to unpack a tuple in several variables.
tuple=(1,2,3,4,5)
n1,n2,n3,n4,n5=tuple
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
