def validate_sorted(data):
    for index, item in enumerate(data):
        if not index:
            continue

        assert item >= data[index-1]
