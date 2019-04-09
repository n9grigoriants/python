
def search4vowels(word):
    """
    Выводит гласные, найденные в веденном слове
    """
    vowels = set('aeiuo')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()
search4vowels()