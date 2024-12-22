class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hindex = len(citations)
        for i in range(len(citations)):
            if(citations[i] < hindex):
                hindex -= 1
            elif(citations[i] >= hindex):
                break
        return hindex