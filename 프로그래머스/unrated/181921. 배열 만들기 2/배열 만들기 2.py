def solution(l, r):
    answer = []
    for i in range(l,r+1):
        stack=0
        value=str(i)
        for j in range(len(value)):
            if value[j]=='0' or value[j]=='5':
                stack+=1
            if stack==len(value):
                answer.append(i)
    if answer == [] :
        answer.append(-1)
    return answer

#집합을 사용하면 더 최적화가능할듯!
# set 사용한 다른사람 풀이
# def solution(l, r):
#     answer = []
#     for num in range(l, r + 1):
#         if not set(str(num)) - set(['0', '5']):
#             answer.append(num)
#     return answer if answer else [-1]