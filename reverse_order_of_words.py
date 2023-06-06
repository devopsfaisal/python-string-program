# Reverse order of Words e.g. My Name is Faisal --> Faisal is Name My

s = input("Enter the string: ")
words = s.split()
print(type(words))

reversed_words_list = words[::-1]
reversed_words = ' '.join(reversed_words_list)

print('Reverse order of words\n', reversed_words)
print(type(reversed_words))
