class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] not in s_set:
                s_set.add(s[right])
                max_length = max(max_length, len(s_set))
            else :
                while(s[right] in s_set):
                    s_set.remove(s[left])
                    left += 1
                s_set.add(s[right])
                max_length = max(max_length, len(s_set))

        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Shrink the window from the left if s[right] is already inside
            while s[right] in s_set:
                s_set.remove(s[left])
                left += 1
            
            # Now we can safely add s[right]
            s_set.add(s[right])
            
            # Update max_length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}  # maps character -> last index in the string
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If we have seen char before and it's inside our current window
            if char in last_index and last_index[char] >= left:
                # Move left pointer to one index beyond the last occurrence of char
                left = last_index[char] + 1
            
            # Update the last index of the current character to the current 'right'
            last_index[char] = right
            
            # The current window is [left ... right]
            max_length = max(max_length, right - left + 1)
        
        return max_length
