class BSTNode:
    def search_range(self, lower_bound, upper_bound):
        chars = []
        print(self.val)
        if self.val.gamertag >= lower_bound and self.val.gamertag <= upper_bound:
            chars.append(self.val)

        if self.val.gamertag < lower_bound and self.right:
            chars.extend(self.right.search_range(lower_bound, upper_bound))
        elif self.val.gamertag > upper_bound and self.left:
            chars.extend(self.left.search_range(lower_bound, upper_bound))
        else:
            if self.left:
                chars.extend(self.left.search_range(lower_bound, upper_bound))
            if self.right:
                chars.extend(self.right.search_range(lower_bound, upper_bound))
        return chars

    # don't touch below this line

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

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
