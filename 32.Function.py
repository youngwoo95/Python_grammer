def open_account(): # 계좌 생성 함수.
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금 함수.
    balance += money
    print(f"{money}원 입금이 완료되었습니다. 잔액은 {balance}원 입니다.")
    return balance

def withdraw(balance, money): # 출금 함수
    if balance >= money:
        balance -= money
        print(f"출금이 완료되었습니다. 잔액은 {balance}원 입니다.")
        return balance
    else:
        print("출금이 완료되지 않았습니다. 잔액이 부족합니다.")
        return balance

def withdarw_night(balance, moeny): # 저녁에 출금.
    commission = 100 # 수수료 100원
    return commission, balance - moeny - commission


open_account()
balance = 0 # 잔액
balance = deposit(balance, 10000)
balance = withdraw(balance, 2000)

(comission, balance) = withdarw_night(balance, 1000)
print(f"수수료 {comission}원 이며, 잔액은 {balance}원 입니다.")

print(balance)