n, k = map(int, input().split())
div = 1000000007

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n*i) % div
    return n

def square(N, p):
    if p ==0:
        return 1
    elif p ==1:
        return N

    tmp = square(N, p//2)
    if p%2:
        return tmp*tmp*N % div
    else:
        return tmp*tmp % div

top = factorial(n)
bot = factorial(k)*factorial(n-k) % div

print((top*square(bot, div-2))%div)