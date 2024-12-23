class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        prod = 1
        for i in range(len(nums)):
            prefix_prod.append(prod)
            prod *= nums[i]
        
        prod = 1
        suffix_prod = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            suffix_prod[i] = prod
            prod *= nums[i]

        prod_ex = [1] * len(nums)
        for i in range(len(nums)):
            prod_ex[i] = prefix_prod[i] * suffix_prod[i]

        return prod_ex