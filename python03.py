# 함수란?

"""

def {함수 이름} ({매개변수}):
    # 내용
    return {반환값}

"""

# a = 10

# def greet(name):
#     return f"Hello, {name}!"

# print(greet("유지원"))

# 매개변수랑 인자

# 인자 : 위치, 기본값, 키워드

# 위치 인자

# def add(a, b, c):
#     return a + b + c

# print(add(3, 5, 8))

# 기본값 인자

# def greet(saying = "Hello", name = "Guest"):
#     return f"{saying}, {name}!"

# print(greet())

# 키워드 인자

# def order(menu = "Pizza", size = "Small"):
#     return f"{size} 사이즈 {menu} 주문 완료"

# print(order(size = "Large"))

# def introduce(name, age=18, city="Seoul"):
#     print(f"이름: {name}")
#     print(f"나이: {age}")
#     print(f"도시: {city}")

# introduce("유지원", city="Daegu")

# def greet(name, age, city):
#     print(name, age, city)

# greet(name="Alice", age=18, city="Daegu")

# 반환값: 함수를 종료신다, 값을 반환한다.

# def square(x):
#     return
#     print(x * x)

# print(square(4))

# 지역 변수, 전역 변수

"""

지역 변수: 함수 내에서 선언된 변수다.
함수 안에서만 사용할 수 있다.
함수 종료와 동시에 소멸된다.

"""
# def func():
#     x = 10 # 지역변수
#     print(x)

# func()

# print(x)

"""

전역 변수: 함수 밖에서 선언된 변수
전체 프로그램에서 "읽을 수 있다".
함수 안에서 전역 변수를 읽을 수는 있지만 수정을 할 수는 없다.

"""

# x = 10
# y = 10
# z = 10
# def func():
#     global x,y,z
#     print(x) # 함수 안에서 값을 읽을 수는 있다.
#     x += 20

# func()
# print(x)

# x = 10  # 전역 변수

# def func():
#     global x
#     x = 20
#     print(x)

# func()
# print(x)

# 재귀함수

# 함수가 자기 자신을 호출하는 함수
# 문제를 작게 쪼개서 풀 때

"""
def {함수 이름}(매개변수):
    if 종료 조건:
        return 결과 <- 기본 케이스에 대한 값: 기저 조건
    
    return {함수 이름}(더 작은 문제) <- 자기 자신을 호출한다.
"""

# 팩토리얼 계산

# 4! -> 4 * 3 * 2 * 1 = 24
# 0! = 1

# def fac(n): # -> n! = n * (n - 1) * ... * 1
#     if n == 0: # -> fac(0) = 1
#         return 1
    
#     return n * fac(n-1) # 더 작은 문제: n! = n * (n - 1) * ... * 1 = n * (n - 1)! -> n * fac(n-1)

"""
4
fac(4)
4*fac(3) : fac(4)
4*3*fac(2) : fac(3)
4*3*2*fac(1) : fac(2)
4*3*2*1*fac(0) : fac(1)
4*3*2*1*1 : fac(0)
4*3*2*1*1 : fac(1)
4*3*2*1 : fac(2)
4*3*2 : fac(3)
4*6 : fac(4)
24
"""

# 피보나치 수열

# 1 1 2 3 5 8 13 ...
# f(n) = f(n-1) + f(n-2)

# def fib(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2) # fib(1) + fib(0)

# for i in range(10):
#     print(fib(i), end = " ")
# """
# fib(3)
# fib(2) + fib(1)
# fib(1) + fib(0) + fib(1)
# 1 + 1 + 1 = 3
# """

# import sys
# sys.setrecursionlimit(10000)

# def bad(n):
#     print(n)
#     return bad(n+1)

# bad(0)

# def func():
#     a = 10
#     print()
#     for i in range():
#         pass
#     while True:
#         pass
#     if 1:
#         pass
#     elif 2:
#         pass
#     else:
#         pass

# sorted(), reversed, map, split, strip, max, min, lambda

# sorted() # 정렬된 새 리스트 반환

# a = [3,1,4]
# b = sorted(a)
# print(b)
# b[0]=5
# print(a, b)

# sort()

# a = [3,1,4]
# a.sort()
# print(a)

# a  = [3,1,4]
# sorted(a)
# print(a)

# def func(x):
#     return -1 * x

# a = [-3,4,1] # -> [3,-4,-1] -> [-4, -1, 3] -> [4,1,-3]
# print(sorted(a))
# print(sorted(a, """key"""))

# a.sort(key=, reverse=)

# a = [3,1,4]
# print(a[::-1])

# split : 문자열을 기준 문자로 나눔

# a = input()
# print(a.split())

# strip : 문자열 양쪽에 공백과 줄바꿈 -> \n

# a = " hello\n "
# print("s",a.strip(),"s",sep="-")

# a = input().split()
# print(a)

# map

"""
map(함수 이름, 반복 가능 객체)
"""

# a = ['3', '5', '7']
# print(a)
# print(list(map(int, a)))

# a = list(map(int, input().split()))
# print(a)

# 변수 N, M, K가 주어진다.

# N, M, K = map(int,input().split())
# print(N, M, K)

# 배열 A가 주어진다.

# A = list(map(int,input().split()))
# print(A)

# filter

# filter(함수 이름, 반복 가능 객체)

# def func(n):
#     return n%2==0

# A = [i for i in range(10)]
# print(list(filter(func, A)))

# min, max

# min : 최솟값
# max : 최댓값

# a = [1,2,3,4,5]

# print(min(a))
# print(max(a))

# 람다함수 혹은 람다식

"""

한 줄 짜리 일회용 함수

"""

# lambda (인수) : 계산식

# A = [i for i in range(10)]
# print(list(filter(lambda n : n%2==0, A)))

# len

# a = list(map(int,input().split()))

# for i in range(len(a)):
#     print(f"a의 {i}번째 값:", a[i])


# 1 2 3 4 5 -> 12345

# a = list(map(int,list(input())))
# print(a)