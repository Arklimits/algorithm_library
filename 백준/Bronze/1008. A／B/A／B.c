#include <stdio.h>

int main() {
    int a;
    double b;

    scanf("%d %lf", &a, &b);

    printf("%.10f\n", a / b);

    return 0;
}