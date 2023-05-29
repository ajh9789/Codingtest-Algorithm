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

#참고할만한거 return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)
# if n % 2 == x % 2 이걸로 짝수일땐 짝수 홀수일땐 홀수 나뉘고
#제곱 부분을 (2 - x % 2)로 처리해서 홀수 짝수 케이스나눔