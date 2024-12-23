class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totaltank = 0
        currenttank = 0
        startidx = 0

        for i in range(len(gas)):
            totaltank += gas[i] - cost[i]
            currenttank += gas[i] - cost[i]

            if(currenttank < 0):
                currenttank = 0
                startidx += 1
        
        if totaltank < 0:
            return -1
        else:
            return startidx