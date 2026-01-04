from itertools import product

def sum_results(user_infos):
    SUM_EMOTICON_PLUS = 0
    SUM_SALES = 0
    for user_info in user_infos:
        if user_info['is_plus'] == 1:
            SUM_EMOTICON_PLUS += 1
        else:
            SUM_SALES += user_info['spend_price']
    return SUM_EMOTICON_PLUS, SUM_SALES

def solution(users, emoticons):
    answer = []
    
    discounts_per_emo = product([10,20,30,40], repeat=len(emoticons))
    MAX_EMOTICON_PLUS = 0
    MAX_SALES = 0
    for discounts in discounts_per_emo:
        user_infos = [{'min_discount':user[0], 'plus_threshold':user[1], 'spend_price':0, 'is_plus':0} for user in users] 
        for discount, emoticon in zip(discounts, emoticons):
            emoticon_price = emoticon * ((100-discount)/100)
            for i, user in enumerate(user_infos):
                
                if user_infos[i]['is_plus'] == 1:
                    continue
                    
                if discount >= user['min_discount']:
                    user_infos[i]['spend_price']+= emoticon_price
                    if user_infos[i]['spend_price'] >= user['plus_threshold']:
                        user_infos[i]['is_plus'] = 1
        
        SUM_EMOTICON_PLUS, SUM_SALES = sum_results(user_infos)
        if MAX_EMOTICON_PLUS < SUM_EMOTICON_PLUS:
            MAX_EMOTICON_PLUS = SUM_EMOTICON_PLUS
            MAX_SALES = SUM_SALES
        elif MAX_EMOTICON_PLUS == SUM_EMOTICON_PLUS and MAX_SALES < SUM_SALES:
            MAX_SALES = SUM_SALES
            
    return [MAX_EMOTICON_PLUS, int(MAX_SALES)]

