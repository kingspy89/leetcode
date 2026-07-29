class Solution(object):
    def reversePrefix(self, word, ch):
        k=""
        if(ch not in word):
            return word
        else:
            j=word.index(ch)
            word=word[:j+1][::-1]+word[j+1:]
        return word