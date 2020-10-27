def sort(data):
    for index, current in enumerate(data):
        least = index
        for index2, check in enumerate(data[index:]):
            if check < data[least]:
                least = index2 + index
        if least != index:
            data[index], data[least] = data[least], data[index]
