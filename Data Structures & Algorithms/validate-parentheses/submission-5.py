class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char == "(" or char =="[" or char == "{":
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]: 
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True