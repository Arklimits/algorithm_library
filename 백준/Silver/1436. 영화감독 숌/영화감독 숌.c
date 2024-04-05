#include <stdio.h>

int main() {
    int n, i, cnt, temp;
    i = 666, cnt = 1;
    scanf("%d", &n);

    while (cnt < n) {
        i++;

        if (i % 1000 == 666) cnt++;
        else{
            temp = i / 10;
            while (temp){
                if (temp % 1000 == 666){
                    cnt++;
                    break;
                }
                else{
                    temp /= 10;
                }
            }

        }

    }

    printf("%d\n", i);
}
