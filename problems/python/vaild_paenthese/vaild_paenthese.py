class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for char in s:

           
            if char in "([{":
                stack.append(char)

            else:
             
                if not stack:
                    return False

                top = stack[-1]

                if mapping[char] == top:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
