android = 'Marvin, the interesting android'
letters = list(android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[7:]:
    print('\t'*2, char)
print()
for char in letters[10:15]:
    print('\t'*3, char)