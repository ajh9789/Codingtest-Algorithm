#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int k) {
    int answer,p = 0;
    if (n>0){
    p = n/10;
    }//서비스로 제외되는 음료수값
    answer = n*12000+(k-p)*2000;
    return answer;
}