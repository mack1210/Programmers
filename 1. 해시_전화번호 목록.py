def solution(phone_book):
    n = len(phone_book)
    answer = True

    for i in range(n-1):
        fo = phone_book[i]
        for j in range(i+1,n):
            la = phone_book[j]
            if (fo in la[:len(fo)]) or (la in fo[:len(la)]):
                # 접두사에만! 해당이 되어야하기때문에!
                answer = False
                return answer
    return answer


## hash 활용 풀이
# def solution(phone_book):
#     answer = True

#     hash_map = {}

#     for phone_number in phone_book:
#         hash_map[phone_number] = 1

#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number

#             if temp in hash_map and temp != phone_number:
#                 return False

#     return answer

phone_book = ["119", "97674223", "1195524421"]

solution(phone_book)
