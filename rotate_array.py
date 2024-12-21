class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums_k = nums[l-k:]
        nums[k:] = nums[:l-k]
        nums[:k] = nums_k