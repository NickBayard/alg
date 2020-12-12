class HashTable:
    def __init__(self, size=127):
        self.back = [None] * size
        self.size = size
        self.length = 0

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        location = self._hash(key)
        if self.get(key) is None:
            self.length += 1
        self.back[location] = key

    def get(self, key):
        location = self._hash(key)
        return self.back[location]


def radix(data):
    h = HashTable()
    for k, _ in data:
        h.insert(k)
    return h.length


def sort(data, rad):
    aux = [None] * len(data)
    count = [0] * (rad+1)

    for k, _ in data:
        count[k+1] += 1

    for index, num in enumerate(count[:-1]):
        count[index+1] += count[index]

    # import pdb; pdb.set_trace()

    for k, v in data:
        aux[count[k]] = (k, v)
        count[k] += 1

    return aux

