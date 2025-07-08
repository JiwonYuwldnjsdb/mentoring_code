# print()

# print("Hello World")

# print()

"""

print(*objects, sep, end)

print(10)
print(3.14)
print("Python")

print("Python", "is", "fun")

"""

# print("Python", "is", "fun", sep="")

# print("Python", end="_") # \n -> 줄바꿈
# print("is", end="_")
# print("fun", end="_")

"""
print("본인의 이름")
print("본인의 나이")
print("본인의 중학교 이름")

# end만 사용을 하세요
"""

# print("본인의 이름", "본인의 나이", "본인의 학교") # 줄바꿈 2번번

# x = input()
# print(x)

# 자료형

# int, float, string, set, list, tuple, dictionary, type()

# type() # 괄호 사이에 들어가는 변수의 자료형을 반환
# type(10) # int
# type("안녕하세요") # string

# print(type("안녕하세요"))

# integer: 정수형
# {변수 이름} = {변수값}

# a = 10

# a = float(input())

# int() 괄호사이에 들어가는 값을 정수로 바꿔줌줌

# print(a, abs(a), type(a))

# abs() 괄호사이에 들어가는 값을 양수로 바꿔줌

# int : 정수형이다.
# int로 만들어주는 함수는 int()가 있다. abs()라는 함수는 값을 양수로 바꿔준다.

# boolean 자료형. 참과 거짓을 나타냄. True, False

# a = False
# print(a, type(a))

# float : 부동소수점형, 소수
# float() 부동소수점형으로 만들어줌.

# a = float(input())
# print(a, type(a), round(a, 2))

# round(val, num): num번째 까지 표시

"""

사용자로부터 정수와 소수를 입력받아서 출력하는 프로그램 작성:

정수는 그 정수의 값과 절댓값을 출력
소수는 그 소수의 값과 절댓값, 소수 3번째 자리에서 반올림한 값.

"""

# string: 문자열

# str() # 괄호에 들어가는 값을 문자열로 바꿔줌.
# a = str(10)

# print(a, type(a))

# split, strip

# split(): 괄호 사이의 문자열을 기준으로 문자열을 나눔.

# a = "Python is fun."
# print(a.split("n")) # 디폴트로 공백 기준

# #strip: 문자열 양쪽의 공백을 제거합니다.

# a = " Python is fun "
# print(a)
# print(a.strip())

# 문자열은 불변 : 바꿀수가 없다. 

# a = a.split()

"""

사용자에게 문장을 입력받아서 공백 기준으로 쪼갠뒤 출력하는 프로그램 작성.

"""

# string: 문자열이다.
# split은 문자열을 기분되는 문자로 쪼갠다.
# strip은 문자열 양끝의 공백을 제거한다.

# list: 배열, 가변 쉬퀀스. 여러개의 자료형을 저장할 수 있음. 서로 다른 종류의 자료형을 저장할 수 있다.
# a = [1, 2, 3] # 대괄호 + 쉽표로 원소 구분
# print(a)
# a.append(4)
# print(a)
# a.extend([5,6])
# print(a)
# print(a.pop())
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# print(a.count(1))
"""

.append(x) : 값 x를 리스트 가장 뒤에 추가
.extend(x) : 리스트 x를 리스트에 확장장
.pop(x) : 리스트의 가장 뒤의 원소를 제거하고 반환함.
.sort(x) : 리스트를 정렬합니다.
.reverse(x) : 리스트를 뒤집습니다.
.count(x) : 리스트에서 값 x의 개수를 센다.

"""

"""

사용자로부터 숫자(0 ~ 9) 여러개를 한줄로, 공백을 기준으로 나뉘어 입력받습니다. -> 정수형으로 바꾸지 마세요. 문자열로 진행행
입력받은 정렬을 하고 뒤집어서 출력한다.

3 2 5 7 4 6

"""

# a = input().split()
# a.sort()
# a.reverse()
# print(a)

# tuple: 리스트 쌍둥이, 불변 -> 바꿀수가 없다.
# a = (1, 2, 3, 4)
# print(a, type(a))

# count 사용 가능하다.

# set: 집합, 순서 없습니다.
# a = {1, 2, 3, 4}
# print(a, type(a))
# # add = append
# # remove = pop
# a.add(5)
# print(a)
# a.remove(5)
# print(a)

# dictionary: 키를 이용해서 값에 접근하는 자료형.

# a = {"a":1, "b":2, "c":3, "d":"sfsdf"}
# print(a, type(a))
# print(a["b"])
# a["c"] = 4
# print(a["c"])
# a["e"] = 5
# print(a["e"])

# 리스트, 튜플, 셋, 딕셔너리

"""

실습1:
사용자에게 숫자를 여러개 입력을 받아서 리스트, 튜플, 셋으로 저장.
출력: 해당 자료형, type

list()
tuple()
set()
a = dict()

실습2:

빈 딕셔너리를 만들어

본인의 이름을 키로 하고 값을 본인의 나이와 중학교를 원소로 가지는 리스트로 하여 저장을 하고 딕셔너리 출력
내년에 본인의 나의가 되도록 값을 키로 접근을 해서 수정으로 하고 다시 출력

"""

# 인덱싱이란? 값의 번째 -> 값에 접근

#    0,1,2,3
# a = [1,2,3,4]
# #  -4,-3,-2,-1
# # print(a[])
# # print(a[-4])

# a[4] = 5
# print(a[4])
# print(a)

# a = {"유지원":[18, "대곽"]}
# print(a)
# a["유지원"][0] = 19
# print(a)

# 슬라이싱: 

# 인덱싱: 자료형(순서가 있는)[인덱스]
# 슬라이싱: 자료형(순서가 있는)[시작:끝:스탭] # 스탭: 디폴트 1

#    0,1,2,3,4,5,6,7,8
# a = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(a[0])
# print(a[0:5:1])
# print(a[0:5:2])

# print(a[0:-1])
# print(a[::2])
# print(a[::-1])

# # .reverse() VS [::-1]
# # reversed() VS [::-1]
# # 객체를 반환     리스트를 반환

# a = [1,2,3,4,5]
# a = list(reversed(a))
# print(a)

"""

배열 a를 만들어서 1부터 10까지 저장

인덱싱을 활용해서 a의 짝수원소들을 출력 + 각 출력값들을 print문 하나만 사용하고 각 출력값 사이는 _ 사용
슬라이싱을 활용해서 a의 홀수원소들을 출력

a를 슬라이싱을 활용해서 역순으로 출력


실습 2

슬라이싱을 활용해서 a의 짝수원소들을 출력
슬라이싱을 활용해서 a의 홀수원소들을 출력

"""