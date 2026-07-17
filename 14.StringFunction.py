# 문자열 처리 함수
python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) # 첫번째 글짜가 대문자인가?
print(python[0].islower()) # 첫번째 글짜가 소문자인가?
print(len(python)) # python 글짜 전체 길이를 반환
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) # n 글짜의 위치를 반환
index = python.index("n", index + 1) # 찾은 글짜와 똑같은 글짜의 다음의 위치\
print(index)


print(python.find("n")) # 얘가 포함된 위치를 알려준다. => 5
print(python.find("Java")) # 없는 글짜는 -1
# print(python.index("Java")) # index 같은 경우는 없는 경우 error

print(python.count("n")) # n 글짜가 총 몇번 등장하는지?
