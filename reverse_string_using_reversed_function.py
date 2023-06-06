#  Reverse of a string using reversed() function
s = input("Enter the String: ")
r = reversed(s)
print(type(r))

# for ch in r:    # Here we can see reversed() return object and we can check the character using for loop.
#     print(ch)   # By uisng join() with empty string we can join the characters into string.

reversed_string = ''.join(r)

print("Reverse of the string is ",reversed_string)
print(type(reversed_string))