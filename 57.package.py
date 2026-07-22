'''
패키지
    - 패키지는 모듈을 디렉터리로 묶어 계층 구조를 만든 것이다.
'''

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# from travel.vietnam import VietnamPackage
#
# trip_to = ThailandPackage()
# trip_to.detail()
#
#
# from travel import vietnam
#
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


#from random import *

from travel import *
#
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
#
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 파일 위치 불러오기.
import inspect
import random

from travel import vietnam

print(inspect.getfile(random))
print(inspect.getfile(thailand))