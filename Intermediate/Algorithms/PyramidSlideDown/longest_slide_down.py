def longest_slide_down(pyramid):
    pyramid = [row[:] for row in pyramid]

    for row in range(len(pyramid) - 2, -1, -1):
        for i in range(len(pyramid[row])):
            pyramid[row][i] += max(
                pyramid[row + 1][i],
                pyramid[row + 1][i + 1]
            )

    return pyramid[0][0]


# Test
print(longest_slide_down([
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]))  # 23

print(longest_slide_down([
    [10],
    [10, 20],
    [10, 10, 20],
    [10, 90, 10, 20]
]))  # 130