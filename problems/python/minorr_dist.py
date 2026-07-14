class Solution(object):
    def mirrorDistance(self, n):
       
        sn=str(n)
        rn=sn[::-1]
        revn=int(rn)
        ans=abs(n-revn)
        return ans