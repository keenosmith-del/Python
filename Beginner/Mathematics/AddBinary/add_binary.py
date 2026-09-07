def add_binary(a, b):
    return bin(a + b)[2:]


# Test
print(add_binary(1, 1))  # "10"
print(add_binary(5, 9))  # "1110"