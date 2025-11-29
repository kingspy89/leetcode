class Solution(object):
    def minOperations(self, nums, k):
        ans=sum(nums)%k
        return ans