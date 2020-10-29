import random


def sort(data, start=0, end=None, shuffle=True):
    if shuffle:
        assert end is None
        assert start == 0
        random.shuffle(data)

    if end is None:
        end = len(data) - 1

    # Start with the second entry
    low, high = start + 1, end

    while low < high:
        # seek left to find first entry greater than first entry
        for low in range(low, high+1):
            if data[low] > data[start]:
                break

        # seek right to find first entry less than first entry
        for high in range(high, start, -1):
            if data[high] < data[start]:
                break

        if low < high:
            data[low], data[high] = data[high], data[low]

    # swap with high (which is now the bottom index of the partition)
    if data[high] < data[start]:
        data[start], data[high] = data[high], data[start]

        if high - start >= 2:
            sort(data, start, high-1, shuffle=False)

        if end - high >= 2:
            sort(data, high+1, end, shuffle=False)
    else:
        sort(data, start + 1, end, shuffle=False)

