class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()  # ignore trailing spaces

        for i in range(len(s), 0, -1):
            if s[i-1] == " ":
                return len(s) - i   # length of last word

        # if no space found, whole string is the last word
        return len(s)
