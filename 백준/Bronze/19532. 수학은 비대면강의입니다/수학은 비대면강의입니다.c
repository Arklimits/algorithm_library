#include <stdio.h>

int main() {
    int a, b, c, d, e, f;

    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);

    printf("%d %d", (c*e-f*b)/(a*e-d*b), (c*d-f*a)/(b*d-e*a));
}
