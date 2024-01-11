def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError("This operation is not supported for given input parameters")
    else:
        return x / y


def modulo(x, y):
    if 0 < y <= x:
        return x % y
    else:
        raise ValueError("This operation is not supported for given input parameters")


def secondPower(x):
    return x * x


def power(x, y):
    if y < 0:
        raise ValueError("This operation is not supported for given input parameters")
    else:
        return float(x ** y)


def secondRadix(x):
    if x <= 0 or int(x) != x:
        raise ValueError("This operation is not supported for given input parameters")
    else:
        return x ** (1 / 2)


def magic(x, y, z, k):
    l = x + k
    m = y + z

    if m == 0:
        raise ValueError("This operation is not supported for given input parameters")
    else:
        return (l / m) + 1


def control(a, x, y, z, k):
    if a == "ADDITION":
        return addition(x, y)

    elif a == "SUBTRACTION":
        return subtraction(x, y)

    elif a == "MULTIPLICATION":
        return multiplication(x, y)

    elif a == "DIVISION":
        return division(x, y)

    elif a == "MOD":
        return modulo(x, y)

    elif a == "SECONDPOWER":
        return secondPower(x)

    elif a == "POWER":
        return power(x, y)

    elif a == "SECONDRADIX":
        return secondRadix(x)

    elif a == "MAGIC":
        return magic(x, y, z, k)

    else:
        raise ValueError("This operation is not supported for given input parameters")
