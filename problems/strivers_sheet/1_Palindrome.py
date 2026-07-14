class Solution(object):
    def isPalindrome(self, s):
        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()

        n = len(new_s)

        for i in range(n // 2):
            if new_s[i] != new_s[n - i - 1]:
                return False

        return True