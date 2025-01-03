class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if (len(pattern) != len(words)):
            return False

        s_map = {}
        p_map = {}

        for i in range(len(words)):
            if words[i] in s_map:
                if s_map[words[i]] != pattern[i]:
                    return False
            
            if pattern[i] in p_map:
                if p_map[pattern[i]] != words[i]:
                    return False

            s_map[words[i]] = pattern[i]
            p_map[pattern[i]] = words[i]
        
        return True