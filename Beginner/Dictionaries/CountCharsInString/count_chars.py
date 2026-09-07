def count(s):
    result = {}

    for char in s:
        result[char] = result.get(char, 0) + 1

    return result


# Test
print(count("aba"))      # {'a': 2, 'b': 1}
print(count("hello"))    # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count(""))         # {}
