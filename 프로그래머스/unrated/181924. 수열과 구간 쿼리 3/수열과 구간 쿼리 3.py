def solution(arr, queries):
    for i in queries :
        arr[i[0]],arr[i[1]]=arr[i[1]],arr[i[0]]
    
    
    answer = arr
    return answer

# def solution(arr, queries):
#     for a,b in queries:
#         arr[a],arr[b]=arr[b],arr[a]
#     return arr