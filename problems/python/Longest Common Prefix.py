strs= ["flower","flow","flight"]
def longestCommonPrefix(strs):
    prefix = strs[0]
    for i in range (1,len(strs)):
        while strs[i].startswith(prefix) == False:
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix
s=longestCommonPrefix(strs)
print(s)
