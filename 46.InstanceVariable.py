# 멤버 변수
# 인스턴스 변수(Instance Variable)
'''
파이썬에서 "멤버 변수"는 클래스나 인스턴스에 소속된 변수를 말하며, 크게 인스턴스 변수와 클래스 변수 두 종류로 나뉜다.
'''

class Unit:
    def __init__(self, name, hp, damage):
        # self.name / self.hp / self.damage : 인스턴스 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린")

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))