nums1=[1,2,3]
nums2=[2,5,6,0,0]
m=3
n=3
for i in range(1,m+n):
    if len(nums1)>m:
        nums1.pop()
    if len(nums2)>n:
        nums2.pop()
nums1[m:]=nums2
nums1.sort()
print(nums1)