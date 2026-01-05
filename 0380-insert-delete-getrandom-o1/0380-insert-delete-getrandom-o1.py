class RandomizedSet:


    def __init__(self):
        self.list = list()
        self.dict = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1

    def remove(self, val: int) -> bool:
        #self.dict = {1:0, 2:1, 3:2}
        #self.list = [1,2,3]

        #remove 2
        
        #self.dict = {1:0, 3:2} - UPD index!
        #self.list = [1,3]

        #self.dict = {1:0, 3:1}
        if val in self.dict:
            #self.list.remove(val) this is a mistake since removing from list will traverse full list O(n)
            lastElement = self.list[-1]
            indexToReplace = self.dict[val]

            self.list[indexToReplace] = lastElement
            self.dict[lastElement] = indexToReplace
            self.list.pop(-1)
            self.dict.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()