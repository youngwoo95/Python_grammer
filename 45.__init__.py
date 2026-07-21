# __init__
'''
__init__ 은 파이썬 클래스의 생성자(초기화 메서드)로, 객체(인스턴스ㅏ)가 생성될 때 자동으로 호출되어 초기 속성값을 설정한다.
'''

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린")
# marine3 = Unit("마린", 40)