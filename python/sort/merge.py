def merge(data_a, data_b):
    result = []

    index_a = index_b = 0

    while index_a < len(data_a) and index_b < len(data_b):
        item_a = data_a[index_a]
        item_b = data_b[index_b]

        if item_a < item_b:
            result.append(item_a)
            index_a += 1
        else:
            result.append(item_b)
            index_b += 1

    # Add remaining entries
    if index_b < len(data_b):
        result.extend(data_b[index_b:])
    elif index_a < len(data_a):
        result.extend(data_a[index_a:])

    return result


def merge_sort(data):
    length = len(data)

    if length == 1:
        return data

    half = length // 2

    return merge(merge_sort(data[:half]), merge_sort(data[half:]))
