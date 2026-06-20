def solution(n, words):
    #round_count: 몇 번째로 말하는지 체크. 한 바퀴 돌 때마다 +1
    round_count = 1
    prev_word = words[0]
    memo = set([prev_word])
    pi = 2
    wi = 1
    while wi < len(words):
        now_word = words[wi]
        if prev_word[-1] != now_word[0] or now_word in memo:
            return [pi, round_count]
        else:
            memo.add(now_word)
        #다음 순서로 넘어가기 전에 현재 단어를 이전 단어로 설정
        prev_word = now_word
        if pi == n: # 한 바퀴 순회가 끝난 경우
            pi = 1
            round_count += 1
        else:
            pi += 1
        wi += 1

    return [0,0]