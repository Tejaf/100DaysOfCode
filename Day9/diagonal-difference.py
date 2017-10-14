'''

    Print the absolute difference between the two sums of the matrix's diagonals as a single integer.
    
'''

def diagonal(arr):
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, len(arr[i])):
            diagonal_1 += (arr[j][j])
            diagonal_2 += (arr[j][i-j])
        break
    return abs(diagonal_1-diagonal_2)

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print (diagonal(arr))