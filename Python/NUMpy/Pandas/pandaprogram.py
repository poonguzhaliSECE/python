import numpy as np
import pandas as pd

#Using List
list1=[1,2,3,4,5]
series1=pd.Series(list1)
print("Using List")
print(series1)
print()
#Using Tuple
tuple1=(1,2,3,4,5)
series2=pd.Series(tuple1)
print("Using Tuple")
print(series2)

#Using Dictionary
dict1={1:'a',2:'b',3:'c'}
series3=pd.Series(dict1)
print("Using Dictionary")
print(series3)
print()

#Using NUMPY
numpy1=np.array([1,2,3,4,5])
print("Using NUMPY")
series4=pd.Series(numpy1)
print(series4)
print()

#Using Scalar
scalar=4
series5=pd.Series(scalar,index=[1, 2, 3, 4, 5])
print("Using Scalar")
print(series5)
print()

#Dictionary DATA FRAME WORK
dict2={'Name':['SK','Poojana','Poova'],'Age':[25,18,18]}
series6=pd.DataFrame(dict2)
print("Using Dictionary DATA FRAME")
print(series6)
print()