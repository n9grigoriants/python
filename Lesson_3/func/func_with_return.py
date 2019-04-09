
def search4vowels(word:str) -> set:
    """
    Выводит гласные, найденные в веденном слове
    """
    vowels = set('aeiuo')
    return vowels.intersection(set(word))
    #return bool(found)#булево
    #return found

res = search4vowels("wwww") # {}
print(res)
l = list()
print(l)
l = [1,2,3,]
print(l)
d = dict()
print(d)
s = set()
print(s)
