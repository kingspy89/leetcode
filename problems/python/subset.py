class Solution:
    def subsets(self, nums):
        n = len(nums)
        result = []

        for mask in range(2 ** n):   
            subset = []

            for i in range(n):       
                if (mask >> i) & 1:  
                    subset.append(nums[i])

            result.append(subset)

        return result
