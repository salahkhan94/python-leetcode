class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr_freq = {}
        for i in range(len(nums)):
            if nums[i] in arr_freq:
                arr_freq[nums[i]] += 1
                if(arr_freq[nums[i]] > len(nums)//2):
                    return nums[i]
            else:
                arr_freq[nums[i]] = 1
                if(len(nums) == 1):
                    return nums[i]
        