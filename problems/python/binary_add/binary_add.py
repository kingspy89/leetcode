a = "1010"
b = "1011"
ans=""
carry=0
for i in range(1,max(len(a),len(b))+1):
    d_a= int(a[-i]) if i<=len(a) else 0
    d_b= int(b[-i]) if i<=len(b) else 0
    total=d_a + d_b + carry
    carry= total //2
    ans=str(total %2) + ans