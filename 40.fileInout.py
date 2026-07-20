# 파일 입출력
#score_file = open("score.txt", "w", encoding="utf8")
#print("수학 : 0", file=score_file)
#print("영어 : 50", file=score_file)
#score_file.close()
from encodings import utf_8

#score_file = open("score.txt", "a", encoding="utf8") # a : append 이어 쓰기.
#score_file.write("과학 : 80")
#score_file.write("\n코딩 : 100") # print는 줄바꿈이 자동인데 .write는 줄바꿈이 자동이 아님.
#score_file.close()

# 파일 읽기
#score_file = open("score.txt","r",encoding="utf_8")
#print(score_file.read())
#score_file.close()

# 한줄씩 읽기
#score_file = open("score.txt","r",encoding="utf_8")
#print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동.
#print(score_file.readline(), end="") # end="" 줄바꿈 안함.
#print(score_file.readline(), end="")
#print(score_file.readline(), end="")
#score_file.close()

# 몇줄인지 모를때
# score_file = open("score.txt","r",encoding="utf_8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 리스트에 넣어서 처리 가능
score_file = open("score.txt","r",encoding="utf_8")
lines = score_file.readlines() # list 형태로 저장.
for line in lines:
    print(line, end="")
score_file.close()


