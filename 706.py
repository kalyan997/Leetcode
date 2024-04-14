class MyHashMap:
    MAX = 10**6 + 5
    def __init__(self):
        self.my_map = [None]* self.MAX

    def put(self, key: int, value: int) -> None:
        self.my_map[key] = value

    def get(self, key: int) -> int:
        if self.my_map[key] is None:
          return -1
        return self.my_map[key]

    def remove(self, key: int) -> None:
        self.my_map[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)