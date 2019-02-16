vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Milliways'
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for kv in sorted(found):
    print(kv,  found[kv])
print(found.items())

for k, v in sorted(found.items()):
    print(k, v)
# for letter in word:
#     if letter in vowels:
#
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)

