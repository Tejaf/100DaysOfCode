'''
    For example, given N = 1041 the function should return 5, 
    because N has binary representation 10000010001 and 
    so its longest binary gap is of length 5.

'''

def binary_gap(number):
    count = 0
    max_gap = 0
    temp_gap = 0
    binary = bin(number)[2:]
    last_index = len(binary) - 1

    for i in range(last_index, 0, -1):
        if binary[i] != '0':
            break
        last_index -= 1
    for i in range(last_index-1, 0, -1):
        if binary[i] == '0':
            count += 1
            temp_gap = count
        else:
            if temp_gap > max_gap:
                max_gap = temp_gap
            count = 0
    return max_gap