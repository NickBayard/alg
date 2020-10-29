import random


def converge(data, start, end):
    # seek left to find first entry greater than first entry
    for low_index in range(start, end+1):
        if data[low_index] > data[0]:
            break

    # seek right to find first entry less than first entry
    for high_index in range(end, start-1, -1):
        if data[high_index] < data[0]:
            break

    return low_index, high_index


def sort(data, shuffle=True):
    if shuffle:
        random.shuffle(data)

    # Start with the second entry
    low, high = 1, len(data) - 1

    while low < high:
        low, high = converge(data, low, high)

        data[low], data[high] = data[high], data[low]
        if low < high:
            low += 1
            high -= 1

    # swap with high (which is now the bottom index of the partition
    data[0], data[high] = data[high], data[0]

    if high > 1:
        sort(data[0:high], shuffle=False)

    if len(data) - high > 1:
        sort(data[high+1:], shuffle=False)
