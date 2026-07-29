class Solution(object):
    def countPartitions(self, nums):
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0:
            return 0
        return n - 1