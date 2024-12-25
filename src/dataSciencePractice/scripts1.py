# Operate over arrays
import numpy as np

#1 exercise - basic operation
lst = [5,10,0,200]
a = np.array(lst)
print(a+5)

#2 exercise - Homogeneity check
lst1=[1,2,3,'test',True,3+2j]
b=np.array(lst1)
print(type(b[0]),type(b[1]),type(b[2]),type(b[3]),type(b[4]),type(b[5]))

#3 exercise - Find array size in bytes
lst2=[1,2,3,4,5]
c = np.array([1, 2, 3, 4])
print(c.nbytes)