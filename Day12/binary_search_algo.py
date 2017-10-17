'''
    Binary search makes an assumption that the array is initially sorted
    Complexity:
        Worst: 0(log(n))
        Best: 0(1)
'''

def binary_search(arr, el):
    arr= sorted(arr)
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid+1:]
    if arr[mid] == el:
        return True
    else:
        if el < arr[mid] :
            return binary_search(left, el)
        else:
            return binary_search(right, el)

print (binary_search([1,2,3,4,5], 9)) # returns false