def solution(a, b):
    case1 = int(f"{a}{b}")
    case2 = a*b*2
    answer = max(case1,case2)
    return answer
#max는 int형끼리 str끼리 비교가능
#answer = abValue if abValue >= baValue else baValue 참고