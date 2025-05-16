import numpy as np
lst=[1,2,3,4,5,6,7,8,9,0,1,2]
arr1=np.array(lst)
print(arr1.ndim)
print(arr1.reshape(12,1))
#(1,12),(12,1),(2,6),(6,2),(3,4),(4,3)