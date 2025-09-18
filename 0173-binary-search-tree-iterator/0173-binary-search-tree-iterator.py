class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.s.append(node)
            node = node.left
    
    def next(self) -> int:
        node = self.s.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.s) > 0