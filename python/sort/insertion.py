def sort(data):
    for index in range(1, len(data)):
        current = index
        for check in range(index - 1, -1, -1):
            if data[check] < data[current]:
                break
            #swap
            data[check], data[current] = data[current], data[check]
            current -= 1
