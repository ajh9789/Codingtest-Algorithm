def solution(numbers, hand):
    right = [0,3]  # 초기 오른손 위치를 '*'로 표시
    left = [2,3]   # 초기 왼손 위치를 '#'으로 표시
    result = ""

    for number in numbers:
        if number ==  1 : 
            number = [0,0]
        if number ==  2 : 
            number = [1,0]
        if number ==  3 : 
            number = [2,0]
        if number ==  4 : 
            number = [0,1]
        if number ==  5 : 
            number = [1,1]
        if number ==  6 : 
            number = [2,1]
        if number ==  7 : 
            number = [0,2]
        if number ==  8 : 
            number = [1,2] 
        if number ==  9 : 
            number = [2,2]
        if number ==  0 : 
            number = [1,3]
            
        if number in [[0,0],[0,1], [0,2]]:
            left = number
            result += "L"
        elif number in [[2,0], [2,1], [2,2]]:
            right = number
            result += "R"
        else:
            # 오른손과 왼손까지의 거리 계산 어차피 제곱이라 절대값으로 넣어도 상관없음
            dist_right = abs(number[0] - right[0]) + abs(number[1] - right[1])
            dist_left = abs(number[0] - left[0]) + abs(number[1] - left[1])
            if dist_right == dist_left:
                # 거리가 같을 경우 
                if hand == "right":
                    right = number
                    result += "R"
                else:
                    left = number
                    result += "L"
            elif dist_right < dist_left:
                # 오른손이 더 가까울 경우
                right = number
                result += "R"
            else:
                # 왼손이 더 가까울 경우
                left = number
                result += "L"
    return result


# 키보드 매핑방법1
#     keypad = {
#         1: (0, 0), 2: (1, 0), 3: (2, 0),
#         4: (0, 1), 5: (1, 1), 6: (2, 1),
#         7: (0, 2), 8: (1, 2), 9: (2, 2),
#         0: (1, 3)
#     }
#     for number in numbers:
#     number_coord = keypad[number]

# 키보드 매핑방법2
#     for number in numbers:
#         # 각 숫자에 대한 좌표 설정
#         number_coords = [
#             [0, 0], [1, 0], [2, 0],
#             [0, 1], [1, 1], [2, 1],
#             [0, 2], [1, 2], [2, 2],
#             [1, 3]  # 0은 (1, 3)에 위치
#         ]
#         number_coord = number_coords[number]