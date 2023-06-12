def solution(a, b, c, d):
    num=''.join(f"{a}{b}{c}{d}")
    num=list(map(int,num))  #튜플을 맵으로 int로 바꾸고 리스트로 묶어줌
    num.sort()
    setnum = set(num)
    if len(setnum)==1: #모두가 같을 경우
        return 1111*num[0]
    if len(setnum)==2: #1122나 1222 2221경우
        if num[1]==num[2]:
            if(num[0]==num[1]):
                return (10*num[0]+num[3])**2
            else:
                return (10*num[3]+num[0])**2
        else:
            return num[2]**2-num[1]**2
        
    if len(setnum)==3 : #1123 1223 1233
        if num[0]==num[1]:
            return num[2]*num[3]
        elif num[1]==num[2]:
            return num[0]*num[3]
        elif num[2]==num[3]:
            return num[0]*num[1]
        
    if len(setnum)==4: #1234
        return num[0]
    
    #다른사람코드 각 숫자별 카운팅
    #counts = [nums.count(i) for i in nums]
        
    
    
