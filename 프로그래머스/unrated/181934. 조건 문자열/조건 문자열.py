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
