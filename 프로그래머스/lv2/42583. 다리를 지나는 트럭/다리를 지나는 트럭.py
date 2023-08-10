from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weight = 0
    bridge = deque([0] * bridge_length)  # 다리를 나타내는 큐 초기화
    truck_weights = deque(truck_weights)  # truck_weights를 deque로 변환
    
    while truck_weights:
        total_weight -= bridge.popleft()  # 가장 앞 트럭을 다리에서 뺌
        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()  # 트럭이 다리에 올라감
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)  # 무게 초과로 트럭 대기
        time += 1
    time += bridge_length  # 마지막 트럭이 다리를 빠져나가는 시간 추가
    
    return time 