cabinet = {3:"유재석", 100:"김태호"}
print(cabinet)
# Dictornary에서 값을 가져오는 방법 1
'''
=> 이 방식은 없는 값이면 ERROR
'''
print(cabinet[3])

# Dictornary에서 값을 가져오는 방법 2
'''
=> 이 방식은 없는 값이면 None 출력
'''
print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))
print(cabinet.get(5, "사용가능")) # 값이 없을때 대신 반환할 값을 정할 수 도 있음.
print(cabinet[100])

# Key가 있는지 확인하는 방법
print(3 in cabinet) # True
print(5 in cabinet) # False

# Key에는 숫자가 아닌 문자열도 가능하다.
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호"

# 있는 key를 넣으면 update
cabinet["A-3"] = "유재석(수정)"
print(cabinet)

# 손님이 갔다
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# Key, Value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)