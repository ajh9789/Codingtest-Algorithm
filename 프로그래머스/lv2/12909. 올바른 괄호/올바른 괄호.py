
def solution(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # 스택 마지막 요소 꺼내서 확인, 비어있으면 #반환
        if char in mapping:
            if stack :
                top_element = stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack