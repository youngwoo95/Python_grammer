# with
'''
with 문은 파이썬의 "컨텍스트 매니저(context manager)"를 사용하는 구문으로, 리소스의 획득과 해제를 자동으로 처리한다.
블록을 벗어날 때 정리(cleanup) 코드가 예외 발생 여부와 관계없이 항상 실행된다.

using 문 인듯.
'''

import pickle

# with open("profile.pickle", "rb") as profile_file:
#     profile = pickle.load(profile_file)
#     print(profile)

#with open("study.txt","w",encoding="utf_8") as study_file:
#    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf_8") as study_file:
    print(study_file.read())
    # print(study_file.readlines())
