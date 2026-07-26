class Solution(object):
    def maximumProduct(self, nums):
        max1 = max2 = max3 = -1000
        min1 = min2 = 1000

        for ele in nums:
            # Update three largest numbers
            if ele >= max1:
                max3 = max2
                max2 = max1
                max1 = ele
            elif ele >= max2:
                max3 = max2
                max2 = ele
            elif ele >= max3:
                max3 = ele

            # Update two smallest numbers
            if ele <= min1:
                min2 = min1
                min1 = ele
            elif ele <= min2:
                min2 = ele

        return max(max1 * max2 * max3, min1 * min2 * max1)