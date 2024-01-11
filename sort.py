def sortNumbers(data, condition):

    if condition == "ASC":
        for i in range(len(data) - 1, 0, -1):
            for j in range(i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    elif condition == "DESC":
        for i in range(len(data) - 1, 0, -1):
            for j in range(i):
                if data[j] < data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError("Invalid input data")

    if condition == 'ASC':
        for i in range(len(data) - 1, 0, -1):
            for j in range(i):
                if weights[j] > weights[j + 1]:
                    weights[j], weights[j + 1] = weights[j + 1], weights[j]
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    elif condition == 'DESC':
        for i in range(len(data) - 1, 0, -1):
            for j in range(i):
                if weights[j] < weights[j + 1]:
                    weights[j], weights[j + 1] = weights[j + 1], weights[j]
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

