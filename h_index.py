class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        hindex = len(citations)
        for i in range(len(citations)):
            if(citations[i] < hindex):
                hindex -= 1
            elif(citations[i] >= hindex):
                break
        return hindex


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        hindex = len(citations)
        for i in range(len(citations)):
            if(hindex > citations[i]):
                hindex -= 1
            elif(citations[i] >= hindex):
                break
        return hindex