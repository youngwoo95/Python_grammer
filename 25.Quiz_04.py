'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 참석자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디어는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용


(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
'''

# shuffle(x)
'''
- 리스트를 제자리에서(in-place) 섞는다.
- 반환값은 None이다. (원본 리스트 자체가 변경됨).
- 리스트만 가능 (튜플처럼 불변 시퀀스는 불가)

import random

nums = [1,2,3,4,5]
random.shuffle(nums)
print(nums) # 예: [3, 1, 5, 2, 4]
'''

#random.sample(population, k)
'''
- 시퀀스에서 중복 없이 k개를 무작위로 뽑아 새 리스르토 반환한다.
- 원본은 변경되지 않는다.
- 리스트, 튜플, range, 문자열 등 다양한 시퀀스에 사용 가능.

import random

nums = [1,2,3,4,5]
picked = random.sample(nums, 3)
print(picked) # 예: [5,1,4]
print(nums) # 원본 그대로 : [1,2,3,4,5]
'''

'''
핵심 차이
shuffle
- 원본 변경
- 개수지정 불가 (전체를 섞음)
- 반환값 : None
- 대상타입 : 리스트만

sample
- 원본 변경 X (새 리스트를 반환)
- 개수 지정 가능 (k개만 뽑음)
- 반환값 : 뽑힌 요소 리스트
- 대상 타입 : 시퀀스 전반
'''

# 내가 푼 답
from random import *
lst = []

for i in range(1,21):
    lst.append(i)

print(lst)
shuffle(lst)
print(lst)

chicken = sample(lst, 1)
coffe = sample(lst, 3)

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {chicken}")
print(f"커피 당첨자 : {coffe}")
print("-- 축하합니다. --")

# 인강에서 푼 답
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users)) # range
users = list(users) # 타입변경
# print(type(users)) # list

print(users) # 섞기 전
shuffle(users) # 섞는다.
print(users) # 섞기 후

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print("-- 축하합니다. --")




