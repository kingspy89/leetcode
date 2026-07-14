class Solution(object):
    def findFinalValue(self, nums, original):
        
        for i in nums:
            
            if original in nums:
                original*=2
        
        return original
