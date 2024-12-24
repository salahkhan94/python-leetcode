class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums_cumulative = []
        for i in range(len(nums)):
            if(i == 0):
                nums_cumulative.append(nums[i])
            else:
                cumsum = nums_cumulative[i-1] + nums[i]
                nums_cumulative.append(cumsum)
        l = len(nums)
        for min_len in range(1, l + 1):
            for start_idx in range(0, l-min_len + 1):
                if start_idx == 0:
                    sub_sum = nums_cumulative[start_idx + min_len - 1]
                else:
                    sub_sum = nums_cumulative[start_idx + min_len - 1] - nums_cumulative[start_idx - 1]

                if(sub_sum >= target):
                    return min_len
                        
        return 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sub = float('inf')
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]

            while (sum >= target):
                min_sub = min(min_sub, right - left + 1)
                sum -= nums[left]
                left += 1
        
        return min_sub if min_sub != float('inf') else 0