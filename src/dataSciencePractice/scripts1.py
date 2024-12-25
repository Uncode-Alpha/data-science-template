# Operate over arrays
import numpy as np
import sys

#1 exercise - basic operation
def exercise1():
    lst = [5,10,0,200]
    a = np.array(lst)
    print(a+5)
    return
#2 exercise - Homogeneity check
def exercise2():
    lst1=[1,2,3,'test',True,3+2j]
    b=np.array(lst1)
    print(type(b[0]),type(b[1]),type(b[2]),type(b[3]),type(b[4]),type(b[5]))
    return
#3 exercise - Find array size in bytes
def exercise3():
    lst2=[1,2,3,4,5]
    c = np.array(lst2)
    print(sys.getsizeof(c))
    return

exercise3()