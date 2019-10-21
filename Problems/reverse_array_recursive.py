def reverse_array(array, start, end):
    if start >= end:
        return array
    array[start], array[end] = array[end], array[start]
    return reverse_array(array, start+1, end-1)

def reverseString(s):
    reverse_array(s, 0, len(s)-1)


array = ['o', 'l', 'l', 'e', 'h']
reverseString(array)
print(array)