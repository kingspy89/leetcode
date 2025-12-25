class Solution(object):
    def findWordsContaining(self, words, x):
        sum=[]
        for i, w in enumerate(words):
            if x in w:
                sum.append(i)
        return sum