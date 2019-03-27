vowels = {'a', 'e', 'i', 'o', 'u'}
word = input()
found = vowels.intersection(set(word))
print(found)
