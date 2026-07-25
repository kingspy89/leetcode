class Solution(object):
    def rearrangeArray(self, nums):
       n = len(nums)
       ans= [0]*n
       pos,neg = 0,1 
       for i in range(n):
         if nums[i] >= 0:
            ans[pos]=nums[i]
            pos +=2
         else:
            ans[neg]= nums[i]
            neg +=2
       return ans