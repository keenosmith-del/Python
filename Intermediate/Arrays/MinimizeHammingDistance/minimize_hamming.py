class Solution:
    def minimumHammingDistance(
        self,
        source: list[int],
        target: list[int],
        allowedSwaps: list[list[int]]
    ) -> int:

        n = len(source)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a

        for a, b in allowedSwaps:
            union(a, b)

        groups = {}

        for i in range(n):
            root = find(i)

            if root not in groups:
                groups[root] = {}

            groups[root][source[i]] = groups[root].get(source[i], 0) + 1

        distance = 0

        for i in range(n):
            root = find(i)
            values = groups[root]

            if values.get(target[i], 0) > 0:
                values[target[i]] -= 1
            else:
                distance += 1

        return distance


solution = Solution()

tests = [
    (
        [1, 2, 3, 4],
        [2, 1, 4, 5],
        [[0, 1], [2, 3]],
        1
    ),
    (
        [1, 2, 3, 4],
        [1, 3, 2, 4],
        [],
        2
    ),
    (
        [5, 1, 2, 4, 3],
        [1, 5, 4, 2, 3],
        [[0, 4], [4, 2], [1, 3], [1, 4]],
        0
    ),
]

for source, target, swaps, expected in tests:
    result = solution.minimumHammingDistance(source, target, swaps)

    print(f"Source:   {source}")
    print(f"Target:   {target}")
    print(f"Swaps:    {swaps}")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    print(f"Passed:   {result == expected}")
    print()
