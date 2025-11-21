class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                top = stack[-1]   # simulate top pointer

                if mapping[char] == top:
                    stack.pop()   # pop top
                else:
                    return False

        return len(stack) == 0