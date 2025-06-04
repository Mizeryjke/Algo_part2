class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    def is_leaf(node):
        return node and node.left is None and node.right is None

    def dfs(node):
        if node is None:
            return 0
        total = 0
        if is_leaf(node.left):
            total += node.left.value
        total += dfs(node.left)
        total += dfs(node.right)
        return total

    return dfs(root)
