#  Reverse of a string without using any python feature
s = input("Enter the String: ")
rev = ''
i = len(s) - 1

while i >= 0:
    rev = rev + s[i]
    i = i - 1

print("Reverse of the string is: ", rev)
print(type(rev))