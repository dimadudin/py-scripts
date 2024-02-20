class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
        load = self.current_load()
        if load >= 0.05:
            new = HashMap(10 * len(self.hashmap))
            for bucket in self.hashmap:
                if bucket:
                    new.insert(bucket[0], bucket[1])
            self.hashmap = new.hashmap

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        load = 0
        for bucket in self.hashmap:
            if bucket:
                load += 1
        return load / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
