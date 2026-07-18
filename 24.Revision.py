# 자료구조의 변형
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu) # SET -> List로 변형
print(menu, type(menu))

menu = tuple(menu) # List -> Tuple로 변형
print(menu, type(menu))

menu = set(menu) # Tuple -> Set로 변형
print(menu, type(menu))

