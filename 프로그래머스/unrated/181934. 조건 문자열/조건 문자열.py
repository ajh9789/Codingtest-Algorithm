def solution(ineq, eq, n, m):
    case1=ineq+eq
    if(case1=="<=") :
        if(n<=m):
            return 1
        else:
            return 0
    if(case1==">=") :
        if(n>=m):
            return 1
        else:
            return 0
    if(case1=="<!") :
        if(n<m):
            return 1
        else:
            return 0
    if(case1==">!") :
        if(n>m):
            return 1
        else:
            return 0
# 참고 return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
#내장 함수 eval을 사용하면 문자열 형태의 코드를 실행할 수 있습니다.