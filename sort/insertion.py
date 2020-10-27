def insertion_sort(data):
    i = current = 1
    while current < len(data):
        while i:
            if data[i] < data[i-1]:
                temp = data[i]
                data[i] = data[i-1]
                data[i-1] = temp
                i -= 1
            else:
                break
        current += 1
        i = current
