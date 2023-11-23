def permutations(array):
    fin = []
    if len(array) == 1:
        return [array]
    elif len(array) == 0:
        return [fin]
    else:
        for i in range(len(array)):
            elem = array[i]
            shorter = array[:i] + array[i + 1:]
            perms = permutations(shorter)
            for p in perms:
                fin.append([elem] + p)
    return fin
