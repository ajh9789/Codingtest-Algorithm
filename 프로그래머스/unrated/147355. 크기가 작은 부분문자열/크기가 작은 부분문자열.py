def solution(t, p):
    t_len = len(t) # 문자열 t의 길이를 저장
    p_len = len(p) # 문자열 p의 길이를 저장
    count = 0   # 결과를 카운트할 변수 초기화
    
    
    for i in range(t_len - p_len + 1): # t에서 길이가 p와 같은 부분문자열을 추출
        sub_str = t[i:i+p_len]  # t에서 길이가 p와 같은 부분문자열 추출
        sub_num = int(sub_str)  # 추출한 부분문자열을 숫자로 변환
        p_num = int(p)           # 문자열 p도 숫자로 변환
        
        if sub_num <= p_num: # 추출한 숫자가 p보다 작거나 같으면 count를 증가
            count += 1
            
    return count  