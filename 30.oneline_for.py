# 한줄로 사용하는 for문

# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함. -> 101, 102, 103, 104.
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 반환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 반환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [i.upper() for i in students]
print(students)

'''
리스트 컴프리헨션(list comprehension)으로, student 리스트의 각 원소에 100을 더해서 새 리스트를 만들고, 그 결과를 다시 student에 대입하는 코드이다.

[동작 원리]
students = [70, 80, 90]
students = [i+100 for i in students]
print(students)

[핵심 포인트]
- i는 student의 각 원소를 순회하는 임시 변수이다.
- [i+100 for i in student]가 완전히 새로운 리스트를 만들고, 그걸 student라는 이름에 다시 할당하는 것이지, 기존 리스트를 직접 수정(in-place)하는 것이 아니다.
- 즉, student = [i+100 for i in student]는 "각 요소에 100을 더한 새 리스트를 만들어서 student 변수가 그걸 가리키게 하라"라는 뜻이다.
'''