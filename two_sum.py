class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[num] = i
        return []
        

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))  
