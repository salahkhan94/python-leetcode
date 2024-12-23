class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while(numbers[i] + numbers[j] != target):
            if(numbers[i] + numbers[j] > target):
                j -= 1
            elif(numbers[i] + numbers[j] < target):
                i += 1
        
        ans = []
        ans.append(i)
        ans.append(j)
        return ans