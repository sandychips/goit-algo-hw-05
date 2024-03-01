class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.hash_table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for item in self.hash_table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.hash_table[index]):
            if item[0] == key:
                del self.hash_table[index][i]
                return True
        return False

# Example usage:
hash_table = HashTable(10)
hash_table.insert(5, "apple")
hash_table.insert(15, "banana")
hash_table.insert(25, "cherry")
print(hash_table.search(15))  # Output: "banana"
hash_table.delete(15)
print(hash_table.search(15))  # Output: None
