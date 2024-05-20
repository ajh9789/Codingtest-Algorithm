#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int price) {
    float dis = 0.0;
    if (price >= 500000) {
        dis = 0.2;
    } else if (price >= 300000) {
        dis = 0.1;
    } else if (price >= 100000) {
        dis = 0.05;
    }

    int answer = price * (1 - dis);
    return answer;
}