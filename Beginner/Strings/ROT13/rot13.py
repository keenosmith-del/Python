def rot13(message):
    result = ""

    for char in message:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char

    return result


# Test
print(rot13("EBG13 rknzcyr."))  # ROT13 example.
print(rot13("This is my first ROT13 excercise!"))
# Guvf vf zl svefg EBG13 rkprepvfr!
