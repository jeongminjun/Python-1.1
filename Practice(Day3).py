### 함수 ###

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.". format(balance))
#         return balance

# # def withdraw_night(balance, money):
# #     commission = 100 # 수수료 100원
# #     return commission, balance - money - commission # 2개의 값을 튜플 형태로 형식으로 리턴 2개의 값을 콤마로 구분해서 반환
    
# def withdraw_night(balance, money):
#     commission  = 100
#     balance = balance - commission - money
#     return commission, balance

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# #balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어: {2}" \
#           .format(name,age,main_lang))
# profile("유재석",20,"파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업. 기본값
# def profile(name, age=17, main_lang= "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어: {2}" \
#           .format(name,age,main_lang))
    
# profile("유재석")
# profile("김태호")

## 함수 호출 변수 순서 상관없음
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name= "유재석", main_lang="파이썬", age= 20)
# profile(main_lang="파이썬", age=25, name= "김태호")

## 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age,*language):
#     print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
    


# profile("유재석",20,"Python","JAva","C","C++","C#","JavaScript")
# profile("김태호",25,"Kotlin","Swift")

### 지역변수와 전역변수
## 지역변수 : 함수 내애서만 쓸 수 있는것
## 전역변수 : 전체에서 쓸 수 있는것

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))


# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# #checkpoint(2) #2명이 경계 근무 나감
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))

# ### Quiz6 ###
# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중
 
#  (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender):

    if gender == "남자":
        s_weight = (0.01*height) * (0.01*height) * 22
        return s_weight,height, gender
    elif gender == "여자":
        s_weight = (0.01*height) * (0.01*height) * 21
        return s_weight,height,gender

s_weight, height, gender = std_weight(height, gender)

input(height, gender)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,s_weight))