# 슬라이싱
jumin =  "990120-1234567"

print(f"성별: {jumin[7]}")
print(f"연: {jumin[0:2]}")
print(f"월: {jumin[2:4]}")
print(f"일: {jumin[4:6]}")

print(f"생년월일: {jumin[:6]}")
print(f"뒤 7자리 : {jumin[7:]}")
print(f"뒤 7자리 (뒤에서부터) {jumin[-7:]}")

if jumin[7] == '1':
    print("남자")
else:
    print("여자")
