class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "(,[,{":
                stack.append(char)
            if char in "},],)":
                if not stack:
                    return False
                top = stack.pop()
                matching = {')': '(', ']': '[', '}': '{'}
                if top != matching[char]:
                    return False
        if stack:
            return False
        return True

