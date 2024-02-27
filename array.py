#this is the practice of arrays
#creation of arrays
import array
arr=array.array("i",[1,2,3,4,6])
print("the new created array is")
for i in range(0, 5):
    print(arr[i], end=" ")
d=array.array("d",[1.1,2.3,6.9])
print("\nthe new created array is")
for j in range(0,3):
    print(d[j], end=" ")
#insertion of elements into arrays
arr.insert(3,90)
print("\narray after insertion is: ", end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print()
#accessing elements of array
print("the element at 0th index is:",arr[0])
print("the element at 1st index is", arr[1])
print("the element at 2nd index is",arr[2])
#removing elements of array using pop method
print("popped element is: ", end=" ")
print(arr.pop(1))
print("array after popping is: ", end=" ")
for i in range(0,len(arr)):
    print(arr[i], end=" ")
#removing elements of array using remove method
arr.remove(6)
print("\narray after removing is: ",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")