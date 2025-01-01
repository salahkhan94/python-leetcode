from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = defaultdict(int)
        for c in ransomNote:
            rn[c] += 1
        mag = defaultdict(int)
        for c in magazine:
            mag[c] += 1
        
        for c in ransomNote:
            if (rn[c] > mag[c]):
                return False
        
        return True