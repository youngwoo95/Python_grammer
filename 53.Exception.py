# 예외처리
'''
try : 예외 발생 가능 코드
except : 예외 처리. 구체적인 예외처리 위에 배치
else : 예외가 없을 때만 실행
finally : 예외 여부와 무관하게 항상 실행
raise : 예외 발생 시키기.


ex)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"0으로 나눌 수 없습니다: {e}")
except (TypeError, ValueError) as e:
    print(f"타입/값 오류: {e}")
except Exception as e:
    print(f"기타 오류: {e}")
else:
    print("예외 없이 성공")   # try 블록이 정상 종료될 때만 실행
finally:
    print("항상 실행")        # 정리 작업(파일 close 등)
'''

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0]/ nums[1]))
    print(f"{int(nums[0])} / {int(nums[1])} = {int(nums[2])}")
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(f"{err}")
except:
    print("알 수 없는 오류가 발생하였습니다.")