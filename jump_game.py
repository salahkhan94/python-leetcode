class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zeros = [i for i in range(len(nums)) if nums[i] == 0]
        if not zeros :
            return True
        max_zero_idx = max(zeros)
        maxidx = 0
        for i in range(len(nums)):
            newidx = nums[i] + i
            if(maxidx < newidx):
                maxidx = newidx
            if(newidx > max_zero_idx):
                return True
            if(i+1 in zeros and maxidx == i+1):
                return False
        return True

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            # If the current position is beyond our max reachable index, we can't proceed further
            if i > max_reach:
                return False
            
            # Update the maximum reachable index
            max_reach = max(max_reach, i + nums[i])
            
            # If we've reached or gone beyond the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return False
