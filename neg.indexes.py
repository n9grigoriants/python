saying = 'Don\'t panic!'
letters = list(saying)

print(letters[0:10:3])
print(letters[3:])
print(letters[:10])
print(letters[::2])#каждая вторая буква

print(letters)
print(letters[0])
print(letters[3])
print(letters[6])
print(letters[-1])
print(letters[-3])
print(letters[-6])

first = letters[0]
last = letters[-1]

# letters[start:stop] #шаг =1
# letters[stop:step]  # по умолчанию используется start = 0
# letters[start::step]#будет использован максимальный индекс

book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
print(booklist[0:3])
print(''.join(booklist[0:3]))
print(''.join(booklist[-6:]))