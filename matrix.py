import numpy as np

N = 10
D = 3

data = np.random.randn(N,D)
#data = np.random.randint(10, size=(N,D))

print(data)

# Extract last 2 columns
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


#print(x)

# Extracts first 2 columns
x = data[:,0:2]
#x = [row[:2] for row in data]
#y = [row[2] for row in data]


#print('x:',x)
#print('y:',y)



