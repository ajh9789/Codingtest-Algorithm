def solution(arr, queries):
    for query in queries :
        s,e,k = query
        for i in range(s,e+1):
            if i==0:    
                arr[i]+=1
            else:
                if i%k==0 :
                    arr[i]+=1
    answer = arr
    return answer