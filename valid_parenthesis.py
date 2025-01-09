def isValid(s: str) -> bool:
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stack = []
    
    for char in s:

        if char in bracket_map.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []
        for ch in s:
            if ch in bracket_map.values():
                stack.append(ch)
            
            else :
                if not stack or stack[-1] != bracket_map[ch]:
                    return False

                stack.pop()
        
        return len(stack)==0


print(isValid("()"))    
print(isValid("()[]{}"))
print(isValid("(]"))    
print(isValid("([])"))  
