
#Wap to print the dimensions and all possible matrix with print mesdage 
'''import numpy as np 
s=[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]
arr=np.array(s)
print(arr,"this is our 3d array matrix")
print("dimension of given matrix is ",arr.ndim,"d")

print(arr.reshape(2,6),"This is our  possiblity for 2d matrix")

print(arr.shape,"This is the shape of our 3D matrix")'''


#Wap to print the dimensions and all possible matrix with print message in 1d
import numpy as np 

s = [[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]
arr = np.array(s)
print(arr, "this is our 3D array matrix")
print("Dimension of given matrix is", arr.ndim, "D")

# Convert to 1D using reshape
arr_1d = arr.reshape(-1)
print("Converted to 1D array using reshape:", arr_1d)
print("Dimension after reshaping is", arr_1d.ndim, "D")
'''for x in np.nditer(arr_1d):
  print(x)#here we apply this func instead of loop'''

x=np.where(arr_1d%2==0)
print(x)


