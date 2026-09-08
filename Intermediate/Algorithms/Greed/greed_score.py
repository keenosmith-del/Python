def score(dice):
    counts = {i: dice.count(i) for i in range(1, 7)}
    total = 0

    for number in range(1, 7):
        triples = counts[number] // 3
        remainder = counts[number] % 3

        if number == 1:
            total += triples * 1000
            total += remainder * 100
        elif number == 5:
            total += triples * 500
            total += remainder * 50
        else:
            total += triples * number * 100

    return total


# Test
print(score([5, 1, 3, 4, 1]))  # 250
print(score([1, 1, 1, 3, 1]))  # 1100
print(score([2, 4, 4, 5, 4]))  # 450

# Pass all tests (v2):
def score_2(dice):
    total = 0

    for number in range(1, 7):
        count = dice.count(number)

        if count >= 3:
            if number == 1:
                total += 1000
            else:
                total += number * 100

            count -= 3

        if number == 1:
            total += count * 100
        elif number == 5:
            total += count * 50

    return total


# Test
print(score_2([5, 1, 3, 4, 1]))  # 250
print(score_2([1, 1, 1, 3, 1]))  # 1100
print(score_2([2, 4, 4, 5, 4]))  # 450
print(score_2([1, 1, 1, 1, 5]))  # 1150
print(score_2([5, 5, 5, 5, 5]))  # 600
print(score_2([5, 5, 2, 3, 6]))  # 100