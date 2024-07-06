import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
result=arr1+arr2
print(result)
print("MINIMUM : ",np.min(arr1))
print("MEAN:",np.mean(arr2))
print("CSUM:",np.cumsum(arr1))
print("PERCENTILE:",np.percentile(arr1,25))
print("PRODUCT:",np.prod(arr1))
print("SLICING:",arr1[:-1])
print("ARRAY INDEX:",arr1[2])