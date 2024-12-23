class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums_map = {}
        for i, n in enumerate(nums) :
            nums_map[n] = i
        
        for i, x in enumerate(nums) :
            for j in range(i+1, len(nums)):
                y = nums[j]
                z = -1 * (x + y)
                if (z in nums_map and nums_map[z] != i and nums_map[z] != j):
                    k = nums_map[z]
                    triplets.append([x, y, z])
        
        return triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)

        for i, x in enumerate(nums):
            left = i+1
            right = len(nums) - 1
            while (left < right) :
                y = nums[left]
                z = nums[right]
                cursum = y + z
                target = -x

                if (cursum < target):
                    left += 1
                elif (cursum > target):
                    right -= 1
                
                elif (cursum == target):
                    left += 1
                    right -= 1
                    triplet = tuple(sorted([x, y, z]))
                    triplets.add(triplet)
                    
        
        return [list(t) for t in triplets]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # If this number is the same as the one before, skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two-pointer search for -nums[i]
            target = -nums[i]
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                cursum = nums[left] + nums[right]
                
                if cursum < target:
                    left += 1
                elif cursum > target:
                    right -= 1
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move left pointer, skipping duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Move right pointer, skipping duplicates
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result
