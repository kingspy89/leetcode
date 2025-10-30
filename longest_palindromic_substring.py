class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
          
            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            
            tmp1 = expand(i, i)
       
            tmp2 = expand(i, i + 1)
            
       
            tmp = tmp1 if len(tmp1) > len(tmp2) else tmp2
            
            if len(tmp) > len(res):
                res = tmp
        return res
