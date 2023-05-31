def solution(num_list):
    return  1 if eval('*'.join([str(n) for n in num_list])) < eval('+'.join([str(n) for n in num_list]))**2 else 0
    #return reduce(lambda x, y: x * y, arr) 
    #기본적으로 초기값을 기준으로 데이터를 루프 돌면서 집계 함수를 계속해서 적용하면서 데이터를 누적하는 방식
    #return eval('*'.join([str(n) for n in arr])) 문자열을 연산시키는 함수 eval 