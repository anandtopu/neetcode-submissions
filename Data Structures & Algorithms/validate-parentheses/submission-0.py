class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == '{':
                stack.append(char)
            elif char == '[':
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
        return not stack


