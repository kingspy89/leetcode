
s='MCMXCIV'
ROMAN = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
romannum=0
for i in range(len(s)):
    romannum+=ROMAN[s[i]]
print(romannum)