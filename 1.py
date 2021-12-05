def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)
 

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp
         
 

def printArray(arr, size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")
arr=[]
n, d = map(int, input().split())
arr=[int(item) for item in input("Enter the list items : ").split()]
leftRotate(arr, d, n)
printArray(arr, n)
