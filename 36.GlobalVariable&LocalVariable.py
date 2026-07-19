# 지역변수 와 전역변수
gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(f"[함수내] 남은 총 : {gun}")

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_return(gun, 2)
print(f"남은 총 : {gun}")