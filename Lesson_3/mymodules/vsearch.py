def search4vowels(phrase: str) -> set:
    """
    Выводит гласные, найденные в веденном слове
    """
    vowels = set('aeiuo')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeoui') -> set:
    """Возвращает множество букв из 'letters', найденных
    в указанной фразе"""
    return set(letters).intersection(set(phrase))


# search4vowels("dsfdsfaa")
# search4vowels("dsfsdfaa")
search4letters("sdfdsfs")
r = search4letters(letters="hello", phrase="hh")# именованные аргументы
r = search4letters("sdfsdf")
print("dsasd", "sdfsdf", sep = " ")