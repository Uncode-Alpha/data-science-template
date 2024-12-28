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

def problem1():
    #Given two arrays do the following
    #1 Create one array with random values
    arr1=[25,56,12,85,34,75]; arr2=[42,3,86,32,856,46]
    randomArray = np.random.randint(0,100,6)
    print("Printing random array of integers with size 6 \n",randomArray)

    #2 Permanently change the dtype of array 1 to complex
    arr1 = np.array(arr1,dtype=complex)
    print("Printing complex array \n",arr1)

    #3 Transform the array into matrices of 2x3 and solve the following equation
    matrix1= np.reshape(arr1,(2,3)); matrix2= np.reshape(arr2,(2,3))
    print("Printing matrix 1 \n",matrix1)
    print("Printing matrix 2 \n",matrix2)
    
    #equation (matrix1^2 - matrix2^2) / (matrix1 - matrix2)
    #Solution:
    #1- we use property of squares (a^2 - b^2) = (a+b)(a-b)
    result=((matrix1+matrix2)*(matrix1-matrix2))/(matrix1-matrix2)
    result2=(np.square(matrix1)-np.square(matrix2))/(matrix1-matrix2)
    print("Printing result of equation \n",result)
    print("Printing alternative result of equation \n",result2)
    return

def problem2():
    #1 Create a 4x4 matrix and add values 4,5,6 above the parent diagonal
    matrix= np.diag([1,2,3],k=1)
    print("Matrix with elements offset by one above the diagonal",matrix)

    #2 Given an array arr=np.arange(11) negate all the elements between 6 and 10
    arr=np.arange(11)
    arr[(arr>6)&(arr<10)]*=-1
    print("Array with elements between 6 and 10 negated",arr)

    #3 Given a matrix mat and an array arr, for each row of the matrix if elements
    #of column 1 are equal to the corresponding element of the array, then print the
    #corresponding value of column 2 of the matrix
    mat = np.array([['abc','A'],['def','B'],['ghi','C'],['jkl','D']])
    arr = np.array(['abc','dfe','ghi','kjl'])
    resultArr=[]
    for i in range(len(mat)):
        if mat[i][0]==arr[i]:
            resultArr=np.append(resultArr,mat[i][1])
    print("Result array",resultArr)
    return




problem2()