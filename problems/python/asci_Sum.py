class Solution(object):
    def scoreOfString(self, s):
        sum=0
        for i in range(1,len(s)):
            sum+=abs(ord(s[i])-ord(s[i-1]))
        return sum
            
        