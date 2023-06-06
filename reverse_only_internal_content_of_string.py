#  Reverse of internal content of word in a string
s = input('Enter the string: ')
l = s.split()
print(l)
l1 = []

for word in l:
    l1.append(word[::-1])

print(l1)

rev_internal_content = ' '.join(l1)

print('Reverse Internal Content:\n', rev_internal_content)