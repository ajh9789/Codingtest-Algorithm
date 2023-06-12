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