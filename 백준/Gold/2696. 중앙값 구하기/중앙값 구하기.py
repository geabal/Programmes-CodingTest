import heapq
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    m = int(input())
    items = []
    for _ in range(m//10+1):
        items += list(map(int, input().split()))

    #중앙값 구하기
    left, right, mids = [], [], [items[0]]
    mid = items[0]

    for i, num in enumerate(items[1:], 1):
        if num < mid:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        if i%2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            mids.append(mid)

    #중앙값 출력
    print(m//2+1)
    for i in range(1, (len(mids)//10)+2):
        if len(mids) - i*10 < 0:
            ans = ' '.join(str(x) for x in mids[(i-1)*10:])
        else:
            ans = ' '.join(str(x) for x in mids[(i-1)*10:i*10])

        print(ans)
