#
# author: F. Coppo
# description: pandas module tutorial ans numpy array tutorial
#

"""
 PANDAS: library for data analysis
"""
print("***************")
print("PANDAS")
print("***************")

import pandas as pd # you have now access to pre-build classses and function: read_csv, DataFrame, Series..

# dataframe from csv/excel
csv_path = "file1.csv"
#df = pd.read_csv(csv_path) # move cvs into dataframe; for excel format is the same


# dataframe from dictionary
df2 = pd.DataFrame( {'a':[31,21,31],'b':[21,22,23], 'c':[1,2,3], 'd':[4,5,6] } )
"""
    a   b  c  d
0  11  21  1  4
1  21  22  2  5
2  31  23  3  6

"""

y = df2[ ['b', 'd']] # sub-dataframe 
print(y)
"""
    b  d
0  21  4
1  22  5
2  23  6
"""

k = df2.ix[2,0] 		# raw 1 column = 2 -> 31
k = df2.ix[2,'c']		# raw 2 column of key 'a' -> 3
k = df2.ix[0:2,'a':'c']	# slice dataframe
"""
    a   b  c
0  11  21  1
1  21  22  2
2  31  23  3
"""

# unique element in a column of dataframe
k = df2['a'].unique() 	# [31, 21] one element has been removed 
k = df2[df2['a'] >= 30] 
"""
    a   b  c  d
0  31  21  1  4
2  31  23  3  6
New dataframe with only sample that have column 'a' grater than 30;
for example if 'a' is weight, you have only sample grater thank 30 kilos
"""

df2.to_csv('new_cvs.cvs') # save the new dataset into csv file

"""
-> to add header:
headers = ["fuel-type","aspiration", "num-of-doors","body-style"]
df.columns = headers

-> datatypes:
print(df.dtypes)
"""



"""
 NUMPY ARRAY: library for scientific computing
	- it contains data of same type
	- used by pandas
	- fast 
	- similar to a list
"""
print("***************")
print("NUMPY ARRAY")
print("***************")

import numpy as np

# 1d, array creation
b = np.array([2, 2, 3, 4, 5.1])
b.size	# array size
b.ndim  # number of numpy array dimension
b.shape # size in each dimension

print(type(b))		# numpy.ndarray
print(b.dtype)		# float 64 bit

# indexing, slicing
b[0] = 1
print(b[0:3])

# basic operation
	
# vector addiction/subtraction
c = np.array([1, 2, 3, 4, 5.1])
print(2*(b + c))       # scalar product              
print(b - c)

"""
NOTE: numpy code vector addiction very simple in comparision with list,
that need iteration:
	for n, m in zip(b,c) 	
		z.appens(n+m))
"""
# vector product
print(b*c)			   # Hadamard product [1*1,2*2,...]

# dot product 
u = np.array([1,2]) 
v = np.array([3,1])

print(np.dot(u,v)) 	   # 1*3 + 2*1
z = u + 1			   # [1+1,2+1]

# universal function
print("u: %s" % u)		   			  # (1 + 2 / 2
print("mean: %s" % u.mean())		  # (1 + 2 / 2
print("max %s" % u.max())
print("standard deviation %s" % u.std()) # array standard deviation sum (a[0] - mean + a[1] - mean + ..)/n

x = np.array([0, np.pi/2, np.pi]) # [0 pi/2 3.14]
print(x)
y = np.sin(x)                     # [0,1,0]

print(np.linspace(-2,2,num=5)) 	  # linspace return evenly spaced number: [-2. -1.  0.  1.  2.]
print(np.linspace(-2,2,num=9)) 	  # linspace return evenly spaced number: [-2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5  2. ]

"""
	PLOT EXAMPLES
"""
print("***************")
print("PLOT EXAMPLE")
print("***************")
# sin plot
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
import matplotlib.pyplot as plt
#plt.plot(x,y)
#plt.show()


# Plotting array
def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
	
u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
Plotvec1(u,z,v)
#plt.show()

"""
	NUMPY 2D ARRAY (matrix)
"""
print("***************")
print("NUMPY 2D ARRAY")
print("***************")
A=np.array([[11,12],[21,22],[31,32]])
type(A) # numpy.ndarray
print(A.shape)                  # (3, 2) tuple
print("array dim: %s" % A.ndim) #  2
print("array size: %s" % A.size)#  6
print(A.dtype) # int64

# element accessing
"""
11 12
21 22
31 32
"""
A[2,0]     # 31
A[1]	   # second row array([21, 22])
A[0][0:2]  # first raw element of column 0 and 1 -> [11 12]
print(A[0:2, 1])  #  element on the first and second rows and second column -> [12 22]

A=np.array([[11,12],[21,22]])
B=np.array([[1, 0],[0,1]])

# sum
Z = A + B 

# multiplication
print(2*B)
"""
[[2 0]
 [0 2]]
"""
print(A*B)
"""
[[11  0]
 [ 0 22]]
"""
print(np.dot(A,B)) # ok if Amxn and Bnxk
"""
[[11 12]
 [21 22]]
"""
print(A.T)  
"""
A.T is transposed:
[[11 21]
 [12 22]]
"""
