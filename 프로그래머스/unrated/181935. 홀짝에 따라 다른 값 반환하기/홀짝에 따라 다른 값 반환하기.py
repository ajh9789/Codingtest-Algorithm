def solution(n):
    hap=0
    if (n%2==1):
        for i in range(n+1) :
            if(i%2==1):
                hap=hap+i
    else : 
        for i in range(n+1) :
            if(i%2==0):
                hap=hap+i*i
    answer=hap
    return answer
# for i in n : 사용했을때
#TypeError: 'int' object is not iterable 
#list([iterable]) 여기서 iterable은 단일 객체가 아닌 반복할 수 있는 문자열, 튜플, 딕셔너리, range() 함수 등을 의미
