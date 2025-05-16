import numpy as np
lst=[[[45,65],[21,23]],[[87,3],[32,6]],[[21,89],[65,74]]]
arr1=np.array(lst)
print(arr1[::2,0:1,1])