def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()
 
def RearrangePosNeg(arr, n):
 
    for i in range(1, n):
        key = arr[i]
 
        # if current element is positive
        # do nothing
        if (key > 0):
            continue
 
        j = i - 1
        while (j >= 0 and arr[j] > 0):
            arr[j + 1] = arr[j]
            j = j - 1
 
        arr[j + 1] = key
 
 
arr=[]
arr=[int(item) for item in input("Enter the list items : ").split()]
n = len(arr)
RearrangePosNeg(arr, n)
printArray(arr, n)
