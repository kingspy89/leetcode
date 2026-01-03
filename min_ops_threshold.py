class Solution(object):
    def minOperations(self, nums, k):
        r=0
        for i in range(len(nums)):
            if (nums[i]<k):
                r+=1
        return r 