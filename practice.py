numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    answer = 0
    global n = len(numbers)
    temp = [0]*n
    case(n)

    return answer

def case(depth):
    if depth == 0:
        return temp
    else:
        temp[n-depth] = numbers[n - depth]
        depth = len(numbers) - 1
        temp += case(depth)
        

solution(numbers, target)