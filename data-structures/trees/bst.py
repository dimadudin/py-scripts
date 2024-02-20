class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if val == self.val:
            return
        if val < self.val:
            if self.left is not None:
                self.left.insert(val)
            self.left = BSTNode(val)
            return
        if self.right is not None:
            self.right.insert(val)
        self.right = BSTNode(val)
        return
