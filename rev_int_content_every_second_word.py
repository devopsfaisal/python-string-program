# Reverse of Internal Content of Every Second Word
s = input('Enter the string: ')
l = s.split()

i = 0
l1 = []

while i < len(l):
    if i % 2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i = i + 1

rev_every_second_internal_content_of_word = ' '.join(l1)

print('Reverse of Internal Content of Every Second Word\n', rev_every_second_internal_content_of_word)
