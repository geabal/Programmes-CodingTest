import sys
input = sys.stdin.readline
def solve():
    a, b, c, d, e, f = map(int, input().split())
    min_n, max_n = -999, 999

    for x in range(min_n, max_n+1):
        for y in range(min_n, max_n+1):
            if (x*a + y*b == c) and (x*d + y*e == f):
                return x, y

x, y = solve()
print(x, y)
