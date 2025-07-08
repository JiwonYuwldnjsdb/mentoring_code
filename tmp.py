n = int(input())

# num = []

# for i in range(n):
#     a = int(input())
#     num.append(a)

# print(num)

num = [int(input()) for i in range(n)]

if 0 not in num:
    print(-1)
elif sum(num) % 3 != 0:
    print(-1)
else:
    num.sort(reverse=True)
    # num = num[::-1]
    print(*num, sep="") # print([1,2,3]) -> print(1,2,3)