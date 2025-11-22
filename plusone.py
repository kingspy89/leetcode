class Solution(object):
    def plusOne(self, digits):
        num = 0
        for d in digits:
            num = num * 10 + d
        num+=1
        lst=[]
        while num > 0:
            lst.append(num % 10)
            num //= 10
        lst.reverse()
        return lst