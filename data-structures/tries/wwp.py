class Trie:
    def words_with_prefix(self, prefix):
        result = []
        current = self.root
        for c in prefix:
            if c not in current:
                return []
            current = current[c]
        self.search_level(current, prefix, result)
        return result

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        keys = sorted(cur.keys())
        for key in keys:
            if key != self.end_symbol:
                self.search_level(cur[key], cur_prefix + key, words)
        return words

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
