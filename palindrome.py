
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        alphnum = re.sub('[\W_]+', '', s)
        alphnum = alphnum.lower()
        l = len(alphnum)
        for i in range(l//2):
            if alphnum[i] != alphnum[l-1-i]:
                return False
        
        return True