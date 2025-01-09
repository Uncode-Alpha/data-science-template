# Operate over arrays
import numpy as np
import sys
#Operate over images
import os
from skimage.io import imread
from skimage import data
import matplotlib.pyplot as plt

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
    
    #4 Given a matrix mat, sort it by the second column
    mat = np.array([[1,21,3],[5,4,2],[56,12,4]])
    sortedMat = mat[mat[:,1].argsort()]
    sortedMat1 = mat[np.argsort(mat[:,1])]
    print("Sorted matrix by second column \n",sortedMat1)
    
    #5 Given an array arr, find the top 4 maximum values
    arr5 = np.array([90, 14, 24, 13, 13, 590, 0, 45, 16, 50])
    maxValue = np.argsort(arr5)[-4:][::-1]
    print("Top 4 maximum values",arr5[maxValue])
    
    #6 Find the nearest number from the given number in an array
    arr6 = np.array([10,55,22,3,6,44,9,54])
    nearest_to = 50
    #Array, take a function to compare each element, take the absolute value
    #We compare the min absolute value associated with the operation
    #We return the number
    nearest = arr6[np.abs(arr6-nearest_to).argmin()]
    print("Nearest number to 50 in array",nearest)
    
    return

def exercise4():
    #1 Given a matrix mat of size 3x3. Find the maximum numbers from each row
    #say N1, N2, and N3. Result in a matrix by adding:
    #Where N1 to the upper half elements of the matrix
    #N2 to the main diagonal elements of mat
    #N3 to the lower half elements of the matrix
    
    # Given a matrix mat of size 3x3
    mat = np.array([[10, 5, 9], [2, 20, 6], [8, 3, 30]]).reshape(3, 3)
    
    # Find the maximum numbers from each column
    n1 = np.max(mat, axis=0)[0]
    n2 = np.max(mat, axis=0)[1]
    n3 = np.max(mat, axis=0)[2]
    
    # Create a new matrix to store the result
    newMat = np.copy(mat)
    
    # Slice the matrix into parts
    # upper is the upper triangular matrix (excluding the main diagonal)
    upper = np.triu_indices(3, 1)
    # diag is the diagonal matrix
    diag = np.diag_indices(3)
    # lower is the lower triangular matrix (excluding the main diagonal)
    lower = np.tril_indices(3, -1)
    
    # Add N1 to the upper half elements of the matrix
    # newMat[upper] accesses the elements at the upper triangular indices
    # += n1 adds the value of n1 to these elements in place
    newMat[upper] += n1
    
    # Add N2 to the main diagonal elements of the matrix
    # newMat[diag] accesses the elements at the diagonal indices
    # += n2 adds the value of n2 to these elements in place
    newMat[diag] += n2
    
    # Add N3 to the lower half elements of the matrix
    # newMat[lower] accesses the elements at the lower triangular indices
    # += n3 adds the value of n3 to these elements in place
    newMat[lower] += n3
    
    # Print the resulting matrix
    print("Solution for matrix operations \n", newMat)
    
    return

def imageExcercise():
    image_path1 = '/Users/josueaguirre/Documents/GitHub/data-science-template/data/dataSciencePractice/DevOps_ToolsWheel.jpeg'
    image_path2 = '/Users/josueaguirre/Documents/GitHub/data-science-template/data/dataSciencePractice/checker_bilevel.png'
    img = imread(os.path.join(data.data_dir, image_path2))
    #print("Image shape",img.shape)
    plt.imshow(img, cmap='gray')
    plt.title('Test Image')
    plt.show()
    return

def imageProblem():
    #1 Upload the image into python environment and show the image
    phantom_path = '/Users/josueaguirre/Documents/GitHub/data-science-template/data/dataSciencePractice/phantom.png'
    image = imread(os.path.join(data.data_dir, phantom_path))
    plt.imshow(image)
    plt.title('Phantom Image')
    plt.axis('off')
    #plt.show()
    
    #2 Perform black and white thresholding with decision boundary set at 0.15. Store the new image in a variable new_img and show it
    #For this we define the threshold value
    threshold = 0.15
    #Values less than or equal to .15 are set to 0 and others equal to 1.
    new_phantom = image.copy()
    
    #when(new_phantom[::0] <= threshold,0,1)
    
    
    #print the new image
    plt.imshow(new_phantom)
    plt.title('Thresholded Phantom Image')
    plt.axis('off')
    plt.show()
    return

def algebraProblem():
    #Solving the next system of linear equations
    #2x+3y+2z=1
    #x+3z=2
    #2x+2y+3z=3
    #We can solve this system of equations using numpy's linear algebra module
    #The system of equations can be represented as a matrix equation
    mat_a=np.array([[2,3,2],[1,0,3],[2,2,3]])
    mat_b=np.array([1,2,3])
    if(np.linalg.det(mat_a)!=0):
        solution = np.linalg.solve(mat_a,mat_b)
    else:
        solution = "No solution, as det is 0"
    print("Solution of the system of equations #1\n",solution)
    
    #Solving the multiplication of the following matrix
    mat_c=np.array([[1,2,3],[4,5,6]])
    mat_d=np.array([[7,8],[9,10],[11,12]])
    
    #We can solve this by using the dot product
    result = np.dot(mat_c,mat_d)
    print("Solution of the matrix multiplication #2\n",result)
    
    #Solving the next system of linear equations, verifying the solution is unique
    #-4x+10y=6
    #2x-5y=3
    #We can solve this system of equations using numpy's linear algebra module
    mat_e =np.array([[-4,10],[2,-5]])
    mat_f =np.array([6,3])
    #We calculate the determinant
    if(np.linalg.det(mat_e)!=0):
        solution = np.linalg.solve(mat_e,mat_f)
        print("The solution is unique\n", solution)
    else:
        print("The solution is not unique as det is 0")
    return
    
    
algebraProblem()