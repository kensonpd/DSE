import numpy as np
#create arrays
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

#basic operations
print("Array a:",a)
print("Array b:",b)
print("Sum of arrays a and b:",np.add(a,b))
print("Difference of arrays a and b:",np.subtract(a,b))
print("Product of arrays a and b:",np.multiply(a,b))
print("Division of arrays a and b:",np.divide(a,b))
print("Square root of arrays a:",np.sqrt(a))
print("Exponential of arrays a:",np.exp(a))


#Aggregation operations
print("Minimum value of array a:",np.min(a))
print("Minimum value of array b:",np.min(b))
print("Mean of array a:",np.mean(a))
print("Standard deviation of array a:",np.std(a))
print("Sum of all the elements in array a: ",np.sum(a))


c=np.array([[1,2],[3,4],[5,6]])
print("Array c:")
print(c)
print("Reshaped array c(2 rows, 3 columns):")
print(np.reshape(c,(2,3)))


d=np.array([[1,2,3],[4,5,6]])
print("Array d:")
print(d)
print("Transposed array d:")
print(np.transpose(d))

