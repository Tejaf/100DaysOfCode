'''
    *Ordered words* - An ordered word is a word in which the letters appear in
    alphabetic order. Take the user input, and order the letters in the word or
    sentence alphabetically. Example: input => "bailey", output = "abeily"
'''

def insertion_sort(itemss):
    items = list(itemss)
    for i in range(1, len(items)):
        j=i
        while j>0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    if isinstance(itemss, str):
        return ''.join(items)
    return items

print (insertion_sort("bailey"))