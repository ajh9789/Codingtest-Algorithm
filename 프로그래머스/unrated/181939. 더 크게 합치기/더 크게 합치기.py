def solution(a, b):
    case1=int(str(a)+str(b))
    case2=int(str(b)+str(a))
    if(case1>case2) :
        fin=case1
    else :
        fin=case2
    return fin
#return int(max(f"{a}{b}", f"{b}{a}"))
