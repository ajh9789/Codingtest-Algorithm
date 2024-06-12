#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string) {
    // 문자열의 길이를 계산합니다.
    int length = strlen(my_string);

    // 변환된 문자열을 저장할 메모리를 동적으로 할당합니다.
    char* answer = (char*)malloc((length + 1) * sizeof(char));
    if (answer == NULL) {
        // 메모리 할당 실패 시 NULL을 반환합니다.
        return NULL;
    }

    // 문자열을 변환합니다.
    int i;
    for (i = 0; i < length; i++) {
        if (my_string[i] >= 'a' && my_string[i] <= 'z') {
            answer[i] = my_string[i] - 32;
        } else if (my_string[i] >= 'A' && my_string[i] <= 'Z') {
            answer[i] = my_string[i] + 32;
        } else {
            // 다른 문자는 그대로 복사합니다.
            answer[i] = my_string[i];
        }
    }
    
    // 널 종단 문자를 추가합니다.
    answer[i] = '\0';
    
    return answer;
}