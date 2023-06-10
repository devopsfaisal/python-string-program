# Program to sort a string first on charactes basis then digits basis
# s = 'B4A1D3'
# output = 'ABD134'

s = input('Enter the string: ')

alphabets = []
digits = []

for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)

# print(alphabets)
# print(digits)

sorted_str = ''.join(sorted(alphabets) + sorted(digits))
print(sorted_str)
