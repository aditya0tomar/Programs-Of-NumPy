#2d-array
# import numpy as np
# lst=[[45,65],[21,23],[87,3],[32,6],[21,89],[65,74]]
# arr1=np.array(lst)
# print(arr1.shape)

#1d-array
import numpy as np
lst=[45,65,21,23]
arr1=np.array(lst)
#print(arr1.shape)

#ReShape
print(arr1.reshape(4,1))
#(1,4),(2,2),(4,1) pssibilities