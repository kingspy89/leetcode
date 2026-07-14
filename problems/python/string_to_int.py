class Solution(object):
  def myAtoi(self, s):
    s=s.lstrip()
    i=0
    num=0
    if not s: 
            return 0
    sign = 1
    if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:] 


    while i < len(s) and s[i].isdigit():
        digit=int(s[i])
        num=num*10+digit
        i+=1
    return sign* num

