import numpy as np

# Creating 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)
print("Dimension:", arr_1d.ndim)
print("Size:", arr_1d.size)

<------------------------>

# Creating 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Dimension:", arr_2d.ndim)
print("Size:", arr_2d.size)

<------------------------>

# Creating 3D array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3D Array:")
print(arr_3d)
print("Shape:", arr_3d.shape)
print("Dimension:", arr_3d.ndim)
print("Size:", arr_3d.size)

<------------------------>

# Array creation routines
# Zeros array
zeros_array = np.zeros((2, 3))
print("\nZeros Array:")
print(zeros_array)

<------------------------>

# Ones array
ones_array = np.ones((3, 2))# Random array
random_array = np.random.random((2, 2))
print("\nRandom Array:")
print(random_array)
print("\nOnes Array:")
print(ones_array) 

<------------------------>

# Identity matrix
identity_matrix = np.identity(3)
print("\nIdentity Matrix:")
print(identity_matrix)

<------------------------>



