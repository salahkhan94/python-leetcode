class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        contiguous = []

        for i in range(len(nums)):
            if i == 0:
                contiguous.append(nums[i])
            elif (nums[i] - nums[i-1] == 1):
                contiguous.append(nums[i])
            
            else :
                if len(contiguous) == 1:
                    output.append(str(contiguous[0]))
                else:
                    output.append(str(contiguous[0]) + "->" + str(contiguous[-1]))
                contiguous.clear()
                contiguous.append(nums[i])
        
        if len(contiguous) != 0 :
            if len(contiguous) == 1:
                output.append(str(contiguous[0]))
            else :
                output.append(str(contiguous[0]) + "->" + str(contiguous[-1]))
        
        return output