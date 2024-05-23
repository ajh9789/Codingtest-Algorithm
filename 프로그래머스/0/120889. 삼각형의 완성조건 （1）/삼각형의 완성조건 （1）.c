#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// sides_len은 배열 sides의 길이입니다.
int solution(int sides[], size_t sides_len) {
    int max=0;
    int hap=0;
    int answer = 2;
    int i;
    for(i=0; i<sides_len; i++){
        hap += sides[i];
        if (sides[i]>max){
            max=sides[i];
        }
    }
    
    if (hap-max>max){
        answer=1;
    }else{
        answer=2;
    }
    return answer;
}