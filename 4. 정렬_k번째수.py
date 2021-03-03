def solution(array, commands):
    lst = []
    T = len(commands)
    for t in range(T):
        command = commands[t]

        i, j, k = command
        temp = array[i-1:j]
        temp.sort()
        lst.append(temp[k-1])
    return lst


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]