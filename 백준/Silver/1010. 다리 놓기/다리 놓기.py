def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

t = int(input())
testcases = []
for i in range(t):
    testcases.append(list(map(int, input().split())))

for west, east in testcases:
    ans = factorial(east) // (factorial(west) * factorial(east - west))
    print(ans)