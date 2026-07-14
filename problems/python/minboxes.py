class Solution(object):
    def minimumBoxes(self, apple, capacity):
         total=sum(apple)
         capacity.sort(reverse=True)
         boxes= 0 
         for c in capacity:
            total-= c
            boxes+=1
            if total<=0:
                break
         return boxes