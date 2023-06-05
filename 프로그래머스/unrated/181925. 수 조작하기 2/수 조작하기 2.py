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




# 참고로 볼만한거
# def solution(log):
#     res=''
#     joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
#     for i in range(1,len(log)):
#         res+=joystick[log[i]-log[i-1]]
#     return res
