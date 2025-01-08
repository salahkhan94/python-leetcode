def isValid(s: str) -> bool:
    # Dictionary that maps closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stack = []
    
    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in bracket_map.values():
            stack.append(char)
        else:
            # If it's a closing bracket, the stack must not be empty
            # and the top of the stack must match the corresponding opening bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    # In the end, the stack must be empty for the string to be valid
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


# Test cases
print(isValid("()"))     # Expected output: True
print(isValid("()[]{}")) # Expected output: True
print(isValid("(]"))     # Expected output: False
print(isValid("([])"))   # Expected output: True
