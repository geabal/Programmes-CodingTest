def solution(phone_book):
    sorted_book = sorted(phone_book)
    book_len = len(phone_book)
    for i, p_num in enumerate(sorted_book):
        if i == book_len -1 :
            return True
        next_p_num = sorted_book[i+1]
        if next_p_num.startswith(p_num):
            return False
    return False