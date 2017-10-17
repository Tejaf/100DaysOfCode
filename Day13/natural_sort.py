import re
'''
    arr = ['a1','a6','a3','a9','a11','a13']
    sort arr numerically
    
    result = ['a1', 'a3', 'a6', 'a9', 'a11', 'a13']
'''

def natural_sort(key):
    convert_to_num = lambda text: int(text) if text.isdigit() else text
    alphanum_key = [convert_to_num(c) for c in re.split(r'(\d+)', key)]
    return alphanum_key

arr = ['a1','a6','a3','b1', 'c3', 'b2', 'a9','a11','a13']
# ar = ["a","b", "c", "A", "B", "C"]
# aa = [1,2,7,2,3,8,9,4,5]
arr.sort(key= lambda a: natural_sort(str(a)))

print (arr) # ['a1', 'a3', 'a6', 'a9', 'a11', 'a13', 'b1', 'b2', 'c3']

