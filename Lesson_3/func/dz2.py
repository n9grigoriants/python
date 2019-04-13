def vote(x: int, y: int, z: int):
    """
    Функция голосования
    :param x:
    :param y:
    :param z:
    :return:
    """
    if (x + y + z) == 0:
        print(0)
    if (x + y + z) == 1:
        print(0)
    if (x + y + z) == 2:
        print(1)
    if (x + y + z) == 3:
        print(1)


x = 0
y = 1
z = 1
vote(x, y, z)
