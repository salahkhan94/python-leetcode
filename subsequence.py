class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lastidx = 0
        for char in s:
            if(char not in t):
                return False
            elif(t.index(char) < lastidx):
                return False
            lastidx = t.index(char)
        
        return True
    


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        l_s = len(s)
        l_t = len(t)
        while(s_pointer < l_s):
            if s[s_pointer] != t[t_pointer]:
                t_pointer += 1
            else : 
                s_pointer += 1
                t_pointer += 1
            if t_pointer == l_t:
                return False

        return True
            
            
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer for s
        i = 0  
        # Pointer for t
        j = 0  

        # While we have characters in both s and t to examine
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
