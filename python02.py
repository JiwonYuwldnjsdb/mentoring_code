# s = "dfsdjfdslfdsjflsdjf"
# age = 18

# print("나이", age, sep=" ")

# # f-string : 문자열 포맷팅

# """"

# f'문자열{age}'


# """

# print(f"나이 {age}")

# # 인덱싱

# 연산자:


"""

산술 연산자

+
-
* : 별
/
** : 별 2개
// : 몫
% : 나머지

"""


# a = 25
# b = 10

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** b)
# print(a // b)
# print(a % b)

# 대입 연산자

"""

= : 값을 할당

a = b : a 에 b를 할당한다.



"""

# a = 10
# a = "sfdsfsf"
# a = .14231

# # 축약연산자

# a = a + 10

# a = 10
# print(a)

# a += 10
# print(a)

"""

+= 
-=
*=
/=
//=
%=
**=

"""

# 비교 연산자

"""

>
>=
<
<=
==
!=

"""

# a = 10
# b = 20

# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)
# print(a == b)
# print(a != b)

# 논리 연산자자

"""

if (조건식):

else

elif


"""

# a = 20
# b = 20

# if a <= b:
#     # 내용
#     print("a 는 b보다 작습니다.")
# elif a== b:
#     print("a는 b와 같습니다.")
# else:
#     print("a는 b보다 큽니다.")

# print("그냥 실행이 됩니다.")

# () -> 먼저 계산

"""

괄호, ** ,*,/,//,% , +,- , > >= < <= == != = /= += -=, not, and, or

"""

# a = 10 + 2 * 5
# print(a)

# or and

"""

(조건식1) or (조건식2)

T T : T
T F : T
F T : T
F F : F


(조건식1) and (조건식2)

T T : T
T F : F
F T : F
F F : F

not 

not (조건식)
조건식
T -> F 
F -> T

"""

# a = 30
# b = 20

# print(a< b)
# print(a== b)

# if not (a < b or a == b): # a <= b
#     print("a는 b보다 큽니다.")
# else:
#     print("a는 b 보다 작거나 같습니다.")

# sdlkjsdflkjsdlkjsdflkjsdlkjsdflkj



"""
         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |
"""

# data = input()
# a = int(input())
# print(data[a-1])

# for 문, while 문

""""

for (변수 이름: x,y,z,   i, j, k) in range(10):
    (내용용)



"""



# range(start, end, step)

# start: 시작, 포함 -> 0
# end: 끝, 포함X -> 
# step: 1,2,-1,-2 -> 1

# a = list(range(10))
# print(a)
# a = list(range(1,10))
# print(a)
# a = list(range(1,10,2))
# print(a)
# a = list(range(10, 0, -1))
# print(a)
# a = list(range(10, 0, -2))
# print(a)


# a = []
# for i in range(10):
#     a.append(i)
# print(a)

# # a = [(변수 이름) for (변수 이름) in (반복가능 객체)]

# a = [i*2 for i in range(10)]
# print(a)

# while (조건식):
#     (내용)

# a = 0
# while a < 10:
#     print(a)
#     a += 1

# break, continue


# break: 반복문 종료


# a = 0
# while True:
#     if a > 10:
#         break
#     a += 1
#     if a % 2 == 0:
#         continue
    
#     print(a)

# for i in range(5):
#     for j in range(5):
#         print(i, j)
