def collatz(x,arr):
    if(x==1):
        arr.append(x)
        return arr
    elif x%2==0:
        arr.append(x)
        x=x/2
        return collatz(x,arr)
    else :
        arr.append(x)
        x=3*x+1
        return collatz(x,arr)


def solution(n):
    answer = []
    return collatz(n,answer)