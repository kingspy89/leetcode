class Solution(object):
    def mySqrt(self, x):
       ans=0
       left,right=1,x
       while left<= right:
            mid = left+(right-left)//2
            sqr=mid*mid
            if sqr == x:
                return mid
            elif sqr < x:
                   ans = mid
                   left = mid + 1
            else:
                right = mid - 1

       return ans
        