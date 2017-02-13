import numpy as np

N = 10  # Number of rows
D = 3   # Number of dimensions or columns

data = np.random.randn(N,D)
print(data.shape)
N1, D1 = data.shape
print (N1, D1)
#data = np.random.randint(10, size=(N,D))

print(data)

# create numpy arrays
x = []
y = []
x = np.array(x)
y = np.array(y)

# Note: row and column indexes start from 0
# Note: List slicing format - start:end:increment - Assumes default if left empty i.e. start = 0, end = end of list, increment = 1

print('Single Row 0',data[0])
print('Every Row Starting from Row 1\n',data[1::])
print('Every Other Row Starting from Row 1\n',data[1::2])

# Read ::,:: as Row slicing then Column slicing for a 2-D array
print('Every Row Starting from Row 1 and only column 1 onwards\n',data[1::,1::])

# Negative Indices are start = start + end e.g -1 + 3 = 2 start position until end
print('Every Row Starting from Row 1 and only the last column\n',data[1::,-1::])

print(data[:, :-1])  # Everything but the last column - 2-D Array
print(data[:, -1]) # Last column only - now 1-D Array
print(data[:, -2])   # 2nd to last column only - 1-D
print(data[:, -3])   # 1st column only - 1-D


#print(x)

# Extracts first 2 columns
x = data[:,0:2]
print(x)
# Using list comprehensions
#x = [row[:2] for row in data]
#y = [row[2] for row in data]

#print('x:',x)
#print('y:',y)

# Extract 1st column and use as boolean operator
X = data[:, -3]
print(X)
Y = data[X < 1]
print(Y)

