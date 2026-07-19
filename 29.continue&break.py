# continue and break
absent = [2, 5] # 결석
no_book = [7] # 책을 가지고 있지 않는 학생.

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break
    else:
        print(f"{student}야 책을 읽어봐.")

