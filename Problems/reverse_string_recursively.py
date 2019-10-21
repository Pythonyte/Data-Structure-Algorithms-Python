def reverse_string(string, start):
    if start == len(string):
        return string
    return reverse_string(string[:start] + string[-1]+ string[start:-1], start+1)


def print_reverse_string(string):
    if len(string) == 0:
        return
    temp = string[0]
    print_reverse_string(string[1:])
    print(temp, end='')


print(reverse_string('sumit', 0))
print(reverse_string('aaaaa', 0))
print(reverse_string('su', 0))
print(reverse_string('aabaa', 0))
print(reverse_string('z', 0))

print_reverse_string('sumit')
print_reverse_string('aaaaa')
print_reverse_string('su')
print_reverse_string('aabaa')
print_reverse_string('z')