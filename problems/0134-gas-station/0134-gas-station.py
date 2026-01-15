class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #[1,2,3,4,5]
        #[3,4,5,1,2]

        # Step 1: Always look for global solution:
        # gas on stations must not be less than needed for the full way
        # if sum(gas) < sum(cost): return -1

        # Step 2: When we fail?
        # if we don't own any gas anymore

        # Step 3: Canonical form
        # We calculate gas we own by summarizing total gain minus loss
        # balance += gain - loss 

        if sum(gas) < sum(cost): return -1
        startPoint = 0
        gasOwned = 0

        for i in range(len(gas)):
            gasOwned += gas[i] - cost[i]
            if gasOwned < 0:
                gasOwned = 0
                startPoint = i + 1

        return startPoint