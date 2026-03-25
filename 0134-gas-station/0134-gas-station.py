class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remainingGas = 0
        startPoint = 0
        
        for i in range(len(gas)):
            remainingGas += gas[i] - cost[i]

            if remainingGas < 0:
                startPoint = i + 1
                remainingGas = 0
                
        if sum(gas) < sum(cost):
            return -1
        return startPoint
        