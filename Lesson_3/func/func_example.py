
def search4vowels():
    """
    Выводит гласные, найденные в веденном слове
    """
    vowels = set('aeiuo')
    word = input("word:")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()
search4vowels()