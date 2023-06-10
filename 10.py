# Input = a4b3c2
# Output = aaaabbbcc
# s = 'a4b3c2'

s = input('Enter any string in this form: ')
output = ''

for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x * d
print(output)