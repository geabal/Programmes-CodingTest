n, k = list(map(int, input().split()))
table = list(input())
ans = 0

for i in range(n):
    if table[i] =='P':
        #i 번째 사람이 먹을 수 있는 햄버거 위치 찾기
        start = max(0, i-k)
        end = min(n-1, i+k) + 1
        for j in range(start, end, 1):
            if table[j] == 'H':
                ans += 1
                table[j] = '_'
                break

print(ans)