def solution(bridge_length, weight, truck_weights):
    passed = []
    on_bridge = [0] * bridge_length
    time = 0

    while(len(truck_weights)):
        temp = on_bridge.pop(0)
        if temp != 0:
            passed.append(temp)
        if sum(on_bridge) + truck_weights[0] <= weight:
            on_bridge.append(truck_weights.pop(0))
        else: on_bridge.append(0)
        time += 1

    return time + bridge_length

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

    

print(solution(bridge_length, weight, truck_weights))