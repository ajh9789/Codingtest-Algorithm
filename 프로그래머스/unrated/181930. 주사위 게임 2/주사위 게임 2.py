def solution(a, b, c):
    if(a!=b and a!=c and b!=c):
        return a+b+c
    elif(a==b and b==c):
        return 3*3*3*a**6
    else:
        return (a+b+c)*(a*a+b*b+c*c)

