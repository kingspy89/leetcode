class Solution(object):
    def recoverOrder(self, order, friends):
        s = set(friends)
        return [o for o in order if o in s]
        