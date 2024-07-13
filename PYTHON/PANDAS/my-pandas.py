import pandas as pd
import numpy as np
print("LIST")
list1=[10,20,30,40]
series1=pd.Series(list1)
print(series1)
print("DICTONARY")
dictonary={'apple':1,'mango':2}
series2=pd.Series(dictonary)
print(series2)
print("TUPLE")
tuple=(1,2,3,4)
series3=pd.Series(tuple)
print(tuple)
print("NUMPY")
num=np.array([1,2,3,4])
series4=pd.Series(num)
print(series4)
print("SCALAR")
series5=pd.Series(5,index=[9,8,7,6])
print(series5)
print("FRAMEWORK")
dict={'Name':['poova','nishanth','sandy'],'age':[18,20,21]}
series6=pd.DataFrame(dict)
print(series6)

