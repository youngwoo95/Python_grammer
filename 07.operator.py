# 연산자
print("===== Operator =====")
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8 => 제곱 연산자
print(5%3) # 2 => 나머지 연산자
print(10%3) # 1 => 나머지 연산자
print(5//3) # 1 => 몫 연산자
print(10//3) # 3 => 몫 연산자

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True (AND 조건)
print((3 > 0) & (3 < 5)) # True (AND 조건)

print((3 > 0) or (3 > 5)) # True (OR 조건)
print((3 > 0) | (3 > 5)) # True (OR 조건)
print(5 > 4 > 3) # True
print(5 > 4 > 7) # False