def soma(x, y):
    """ Soma x e y

    >>> soma(10, 20)
    31

    >>> soma(20, 30)
    50

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float

    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y


def subtrai(x, y):
    """Subtrai x e y

    >>> subtrai(10, 5)
    5
    
    """


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return "O programa não pode ser executado, pois {}".format(e)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)