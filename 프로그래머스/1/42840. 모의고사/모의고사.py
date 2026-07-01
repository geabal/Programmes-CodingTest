def solution(answers):
    answer = []
    
    m1,m2,m3= 0,0,0
    pat1 = [1,2,3,4,5]
    pat2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pat3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len1, len2, len3 = len(pat1), len(pat2), len(pat3)
    
    i1, i2, i3 = 0, 0, 0
    for a in answers:
        if pat1[i1] == a: m1 +=1
        if pat2[i2] == a: m2 +=1
        if pat3[i3] == a: m3 +=1
        
        
        i1 += 1
        i2 += 1
        i3 += 1
        if i1 == len1: i1 = 0
        if i2 == len2: i2 = 0
        if i3 == len3: i3 = 0
    
    score = [m1,m2,m3]
    max_score = max(score)
    for i in range(3):
        if max_score == score[i]:
            answer.append(i+1)
    
    return answer