#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len, int height) {
    int answer,i,count = 0;
    for (i=0;i<array_len;i++){
    if (array[i]>height){
            count++;
        }
    }
    answer=count;
    return answer;
}