#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len, int n) {
    int answer,count,i = 0;
    for (i=0;i<array_len;i++){
        if (array[i]==n){
            count++;
        }
    }
    answer=count;
    return answer;
}