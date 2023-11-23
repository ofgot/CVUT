def polyEval(polynom, x):
    final_result = 0
    parametr = x

    for i in range(len(polynom)):
        final_result += polynom[i] * (parametr ** i)
    return final_result


def polySum(poly1, poly2):

    final_result = []

    if len(poly1) < len(poly2):
        while len(poly1) != len(poly2):
            poly1.append(0)
    else:
        while len(poly1) != len(poly2):
            poly2.append(0)

    for i in range(len(poly1)):
        final_result.append(poly1[i] + poly2[i])

    for i in range(len(final_result) - 1, -1, -1):
        if final_result[i] == 0 or final_result[i] == 0.0:
            final_result.pop(i)
        else:
            break

    return final_result


def polyMultiply(poly1, poly2):

    products = []
    multiply = []
    final = []
    number = 0

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            multiply.append(poly1[i] * poly2[j])
        y = multiply.copy()
        products.extend([y])
        multiply.clear()

    for i in range(1, len(products)):
        products[i] = [0] * i + products[i]

    in_length = len(products[i])  # length of the biggest list inside the products list
    out_length = len(products)    # list length

    for i in range(out_length):
        while len(products[i]) != in_length:
            products[i] = products[i] + [0]

    for j in range(len(products[i])):
        for i in range(out_length):
            number += products[i][j]
        final.append(number)
        number = 0

    return final


