def filter_list(l):
    return [item for item in l if not isinstance(item, str)]


# Test
print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
