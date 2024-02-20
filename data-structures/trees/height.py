class BSTNode:
    def height(self):
        print(self.val)
        if self.val is None:
            return 0
        if self.left:
            left_h = self.left.height()
        else:
            left_h = 0
        if self.right:
            right_h = self.right.height()
        else:
            right_h = 0
        return max(left_h, right_h) + 1

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
