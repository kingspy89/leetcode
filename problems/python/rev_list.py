nums=[1,2,3,4,5]
k=2

trim=nums[::-1][:k]
for i in range(len(nums)-k):
                trim.append(nums[i])
print(trim)