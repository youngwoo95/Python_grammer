# 피클
'''
파이썬 피클(pickle)은 파이썬 객체를 바이트 스트림으로 직렬화(serialize)하고, 다시 객체로 역직렬화(deserialize)하는 표준라이브러리이다.
'''

# import pickle
# profile_file = open("profile.pickle", "wb") # w: 쓰기 b: binary
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
# profile_file.close()

import pickle
profile_file = open("profile.pickle", "rb") # r: 읽기 b: binary
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기.
print(profile)

profile_file.close()
