# module
'''
파이썬 모듈은 함수, 클래스, 변수 등을 담은 .py 파일이다.
'''

# import theater_module as tm
# tm.price(3) # 3명이서 영화 보러 갔을때 가격
# tm.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# tm.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)


# 원하는것만 가져다 쓸 수 있음.
'''
from theater_module import price, price_morningprice(3)
price_morning(4)
# price_soldier(5) # 안됨
'''
from theater_module import price_soldier as ps
ps(5)

