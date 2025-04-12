import numpy as np
'''
arr = np.array( [[ 1, 2, 3],[ 4, 2, 5]] )
print("Array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)

#finding the size of each item in the array
a = np.array([[1,2,3]])
print("Each item contains",a.itemsize,"bytes")

#bitwise operator
a = 25
b = 12
print("binary representation of a:",bin(a))
print("binary representation of b:",bin(b))
print("Bitwise of a and b: ",np.bitwise_and(a,
b))
'''
'''
#sring functions
print("Printing a string multiple times:")
print(np.char.multiply("hello ",3))

print("\n")
print("Converting string into title cased version...")
print(np.char.title("welcome to dr subhash university"))

print("\n")
print(np.char.replace("Welcome javatpoint", "javatpoint","python"))

print("\n")
print(np.char.add(['hello'],['xyz']))

print("\n")
print(np.char.lower(['XYZ', 'FOR']))
print(np.char.upper('subhash'))
print(np.char.capitalize('hello world'))

print("\n")
a=np.char.equal('Dr','Subhash')
print(a)

print("\n")
# np.char.center(arr, width,fillchar)
print(np.char.center('hello', 20,fillchar = '*'))

print("\n")
a=np.array(['xyz', 'for', 'xyz'])
print(np.char.count(a,'xyz'))
print(np.char.count(a,'jjh'))

print("\n")
str = " welcome to javatpoint "
print(np.char.strip(str))

print("\n")
print(np.char.isnumeric('demo'))
print(np.char.isnumeric('12demo'))
print(np.char.isnumeric('12'))

print("\n")
string ='DRSUBHASHUNIVERSITY'
print(string.isupper())
string ='drsubhashuniversity'
print(string.islower())
'''

import math

#math functions
arr = [1,2,3,4,5]
print ("Input array: ", arr)
Sin_Values = np.sin(arr)
print ("Sine values: ", Sin_Values)

cos_Values = np.cos(arr)
print ("cos values : \n", cos_Values)

tan_Values = np.tan(arr)
print ("Tan values : \n", tan_Values)

#Inverse of sin,cos,tan
s = np.arcsin(Sin_Values)
print("\narcsin : ",s)
print(np.degrees(s))

c = np.arccos(cos_Values)
print("\narccos : ",c)
print(np.degrees(c))

t = np.arctan(tan_Values)
print("\narctan : ",t)
print(np.degrees(t))

arr2 = [2.1, 3.29, 4.3, 8.3, 5.6]
print(np.around(arr2))
print(np.around(arr2, decimals = 1))

print(np.floor(arr2))
print(np.ceil(arr2))
