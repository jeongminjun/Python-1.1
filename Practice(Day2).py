# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20 
# subway3 = 30

'''subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐

subway.append("하하")
print(subway)

#정형동씨를 유재석/ 조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
#print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
#print(num_list)

#모두 지우기
#num_list.clear()
#print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호",20,True]
#print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)'''


'''### 사전 ###

cabinet = {3:"유재석",100:"김태호"}
#print(cabinet[3])
#print(cabinet[100])

#print(cabinet.get(3))
#print(cabinet[5])
#print(cabinet.get(5))  #none이 출력된다
#print(cabinet.get(5,"사용가능"))
#print("hi")

#print(3 in cabinet) # True
#print(5 in cabinet) #False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

### 튜플 ###

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")  #안됨

#name = "김종국"
#age = 20
#hobby = "코딩"
#print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

### 세트 ###
# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 ( java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python 은 할 줄 모르는 개발자)
print( java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)

#자료구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu,type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))'''

'''### Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다. --

(활용 예제)'''

'''from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 3))'''

# ## 내가 푼 답 ##
# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(lst)

# shuffle(lst)
# winners = sample(lst, 4)

# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("축하합니다")

# ## 나도코딩 정답 ##

# from random import *

# users = range(1,21) # 1부터 20까지 숫자를 생성
# #print(type(users))
# users = list(users)
# #print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("축하합니다")

### if ###

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp :
#     print("너무 더워요, 나가지 마세요.")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요, 나가지 마세요")

### 반복문(for) ###

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")

# #rnadrange()
# for waiting_no in range(1,6): # 1,2,3,4,5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# print(type(starbucks))

# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

### 반복문(While) ###

# customer = "thor"
# index = 5
# while index >=1 :
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

## 무한루프 ##

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# ## 반복문 빠져나오기 ##
# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

## continue, break ##

# absent = [2,5] #결석
# no_book = [7] # 책을 깜빡했음

# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

## 한 줄 for 문 ##
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101,102,103,104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

### 퀴즈 5 ###

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [O] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

# from random import *

# customer = range(1,51)
# customer = list(customer)

# count = 0 # 총 탑승 승객 수
# for i in customer:  # 1~50 이라는 수 (승객)
#     customer_time = randrange(5,51)
#     if 5<=customer_time<=15 :
#         print("[O] {0}번째 손님 (소요시간 : {1})".format(i,customer_time))
#         count += 1

#     elif 15 < customer_time:
#         print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,customer_time))
    
# print("총 탑승 승객 : {}분".format(count))







