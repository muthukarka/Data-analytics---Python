import numpy as np

#   Iteration arrays 1D & 2D
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

#Iterations in 3D
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
        print(z)

#nditer()
#The function nditer() is a helping function that can be used from very basic to very advanced iterations
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

#Array Join
#Joining means putting contents of two or more arrays in a single array.
#In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
#We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#Array join stack
#Stacking is same as concatenation, the only difference is that stacking is done along a new axis
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
arr = np.hstack((arr1, arr2))
arr = np.vstack((arr1, arr2))
arr = np.dstack((arr1, arr2))

#Numpy split - Splitting is reverse operation of Joining.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.array_split(arr, 4)

#Numpy Split 2D Arrays
# Below code returns three 2-D arrays.

import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

