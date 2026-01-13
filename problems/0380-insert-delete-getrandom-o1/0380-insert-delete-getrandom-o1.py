class RandomizedSet:


    def __init__(self):
        self.list = list() #self.list = [val0, val1, val2] each value will have coresponded index same as in dict
        self.dict = dict() #self.dict = {val0:index0, val1:index1, val2:index2}
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1 #we add element to the dict with the same index from list

    def remove(self, val: int) -> bool:
        #self.dict = {1:0, 2:1, 3:2}
        #self.list = [1,2,3]

        #remove 2
        
        #self.dict = {1:0, 3:2} - UPD index!
        #self.list = [1,3]

        #self.dict = {1:0, 3:1}
        if val in self.dict:
            #self.list.remove(val) is impossible by complexity constraint O(n)
            lastElement = self.list[-1]
            indexToReplace = self.dict[val]

            self.list[indexToReplace] = lastElement #overwrite the needed val memory cell with the last element
            self.dict[lastElement] = indexToReplace #important! updated index in the dict as well
            self.list.pop(-1) # finally remove element from list and dict
            self.dict.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list) # return random value from list without a need to convert keys of dict to list
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()