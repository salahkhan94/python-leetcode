import random

class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []        

    def insert(self, val: int) -> bool:
        if val in self.data_map : 
            return False
        
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map : 
            return False

        val_pos = self.data_map[val]
        self.data[val_pos] = self.data[-1]
        self.data_map[self.data[-1]] = val_pos
        
        self.data.pop()
        self.data_map.pop(val)

        return True

    def getRandom(self) -> int:
        random.choice(self.data)





class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []        

    def insert(self, val: int) -> bool:
        if val in self.data_map : 
            return False
        
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map : 
            return False

        val_pos = self.data_map[val]
        self.data[val_pos] = self.data[-1]
        self.data_map[self.data[-1]] = val_pos
        
        self.data.pop()
        self.data_map.pop(val)

        return True

    def getRandom(self) -> int:
        random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()