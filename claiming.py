class Solution(object):
    def climbStairs(self, n):
        step=n
        for i in range(n,0,-1):
            if i >1:
                step=step-2
            else:
                step=step-1
        return step
                

    
