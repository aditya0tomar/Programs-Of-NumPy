import numpy as np
s=[[1,2,3,4]]
arr=np.array(s)
s1=[[5,6,7,8]]
arr1=np.array(s1)
arr3=np.concatenate((arr,arr1),axis=1)
print(arr3)