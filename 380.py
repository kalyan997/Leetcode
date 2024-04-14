class RandomizedSet:

    def __init__(self):
        self.my_set = set()
        

    def insert(self, val: int) -> bool:
        not_present = True
        if val not in self.my_set:
            self.my_set.add(val)
        else:
            not_present = False
        return not_present
        

    def remove(self, val: int) -> bool:
        present = True
        if val in self.my_set:
            self.my_set.remove(val)
        else:
            present = False
        return present
        

    def getRandom(self) -> int:
        random_element = random.choice(tuple(self.my_set))
        return random_element

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()