class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer

            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            if total_sum // total_count == node.val:
                answer += 1

            return total_sum, total_count

        dfs(root)
        return answer


solution = Solution()

# Example 1:
#        4
#       / \
#      8   5
#     / \   \
#    0   1   6

root = TreeNode(
    4,
    TreeNode(
        8,
        TreeNode(0),
        TreeNode(1)
    ),
    TreeNode(
        5,
        None,
        TreeNode(6)
    )
)

print(solution.averageOfSubtree(root))  # 5


# Example 2:
root = TreeNode(1)

print(solution.averageOfSubtree(root))  # 1
