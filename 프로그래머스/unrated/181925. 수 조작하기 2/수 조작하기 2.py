def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        if i==0: 
            continue
        elif i==len(numLog):
            break
        elif numLog[i]-numLog[i-1] == 1:
            answer=answer+'w'
        elif numLog[i]-numLog[i-1] == -1:
            answer=answer+'s'
        elif numLog[i]-numLog[i-1] == 10:
            answer=answer+'d'
        elif numLog[i]-numLog[i-1] == -10:
            answer=answer+'a'            
    return answer