import numpy as np

# Creating arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([5, 15, 25, 35, 45])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Element-wise Addition
add_result = np.add(arr1, arr2)
print("\nAddition:", add_result)

# Element-wise Subtraction
sub_result = np.subtract(arr1, arr2)
print("Subtraction:", sub_result)

# Element-wise Multiplication
mul_result = np.multiply(arr1, arr2)
print("Multiplication:", mul_result)

# Element-wise Division
div_result = np.divide(arr1, arr2)
print("Division:", div_result)

# Square Root of elements in arr1
sqrt_result = np.sqrt(arr1)
print("\nSquare root of arr1:", sqrt_result)

# Mean and Standard Deviation
print("\nMean of arr1:", np.mean(arr1))
print("Standard Deviation of arr1:", np.std(arr1))

# Maximum and Minimum
print("\nMaximum value in arr1:", np.max(arr1))
print("Minimum value in arr1:", np.min(arr1))
