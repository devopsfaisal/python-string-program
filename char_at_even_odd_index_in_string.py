# Program to print characters at even and odd index in the string separately

s = input('Enter the string: ')

i = 0
print('The Characters present at even index: ')
while i < len(s):
    print(s[i])
    i += 2

i = 1
print('The Characters present at odd index: ')
while i < len(s):
    print(s[i])
    i += 2