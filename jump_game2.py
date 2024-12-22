class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentend = 0
        furthest = 0
        for i in range(len(nums)-1):
            furthest = max(furthest, i + nums[i])
            if i == currentend:
                currentend = furthest
                jumps += 1
        return jumps