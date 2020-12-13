def sort(data, rad):
    aux = [None] * len(data)
    count = [0] * (rad+1)

    # count characters
    for k, _ in data:
        count[k+1] += 1

    # convet count to index
    for index, num in enumerate(count[:-1]):
        count[index+1] += count[index]

    # distribute
    for k, v in data:
        aux[count[k]] = (k, v)
        count[k] += 1

    return aux


class Alphabet:
    def __init__(self, primitives):
        self.primitives = primitives
        self.map = {x:l for x, l in enumerate(primitives)}
        self.radix = len(self.map)

    def toChar(self, index):
        return self.map[index]

    def toIndex(self, character):
        for index, c in self.map.items():
            if c == character:
                break
        else:
            raise KeyError('uh oh')

        return index


def multi_sort(data, width, alphabets):
    aux = [None] * len(data)

    for w in range(width-1, -1, -1):
        alphabet = alphabets[w]
        radix = alphabet.radix

        count = [0] * (radix+1)

        # count characters
        for word in data:
            key = word[w]
            index = alphabet.toIndex(key)
            count[index+1] += 1

        # convert to index
        for index, num in enumerate(count[:-1]):
            count[index+1] += count[index]

        # distribute
        for word in data:
            key = word[w]
            index = alphabet.toIndex(key)
            aux[count[index]] = word
            count[index] += 1

        # copy back
        for index, word in enumerate(aux):
            data[index] = word
