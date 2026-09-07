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
print(rot13("hello"))          # uryyb
print(rot13("Hello, World!"))  # Uryyb, Jbeyq!
print(rot13("Hello 123!"))     # Uryyb 123!
