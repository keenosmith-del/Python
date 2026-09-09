class Solution:
    def twoEditWords(
        self,
        queries: list[str],
        dictionary: list[str]
    ) -> list[str]:
        result = []

        for query in queries:
            for word in dictionary:
                differences = 0

                for a, b in zip(query, word):
                    if a != b:
                        differences += 1

                        if differences > 2:
                            break

                if differences <= 2:
                    result.append(query)
                    break

        return result


solution = Solution()

tests = [
    (
        ["word", "note", "ants", "wood"],
        ["wood", "joke", "moat"],
        ["word", "note", "wood"]
    ),
    (
        ["yes"],
        ["not"],
        []
    ),
    (
        ["abc", "xyz", "hello"],
        ["abd", "xya", "heppo"],
        ["abc", "xyz", "hello"]
    ),
]

for queries, dictionary, expected in tests:
    result = solution.twoEditWords(queries, dictionary)

    print(f"Queries:    {queries}")
    print(f"Dictionary: {dictionary}")
    print(f"Expected:   {expected}")
    print(f"Result:     {result}")
    print(f"Passed:     {result == expected}")
    print()
