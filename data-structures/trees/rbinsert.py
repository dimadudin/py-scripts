class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new = RBNode(val)
        new.parent = None
        new.left = self.nil
        new.right = self.nil
        new.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            elif val == current.val:
                return

        new.parent = parent
        if not parent:
            self.root = new
        else:
            if val < parent.val:
                parent.left = new
            elif val > parent.val:
                parent.right = new
