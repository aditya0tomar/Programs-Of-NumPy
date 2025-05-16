#WAP TO PRINT THE MATRIX AND SHOW THAT ANY GIVEN ELEMENT FROM USER IS PRESENT IN MATRIX IF IT IS PRESENT THEN COUNT HOW MANY TIMES COME IN MATRIX

import numpy as np

# Make 2D array in Python
L1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(L1, "is matrix L1")

# Input from user
b = int(input("Enter the number you want to check in L1: "))

# Check if number exists in L1
if b in L1:
    print("YES, IT IS PRESENT IN L1")
else:
    print("NO, IT IS NOT PRESENT IN L1")

# Count occurrences of the number in the array
count = L1.count(b)

print(f"{b} appears {count} time in L1")


#WAP TO PRINT THE WHICH NUM IS ODD AND EVEN INSIDE OF MATRIX
'''
import numpy as np
L1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(L1,'its a matrix of L1')
print("BELOW WE REMOVE ALL ELEMENTS FROM ARRAY SO WE ARE ABLE TO CHECK WHICH IS ODD AND EVEN")
for i in L1:
    for j in i:
        if j % 2==0:
            print(j,"is even number")
        else:
            print(j,"is odd number")'''