#include <stdio.h>
#include <stdlib.h>

int compare(const int *a, const int *b) {
    return (*b - *a);
}

int main() {
    int n, i;
    int x[10];

    scanf("%d", &n);

    i = 0;
    while (n > 0) {
        x[i++] = n % 10;
        n /= 10;
    }

    qsort(x, i, sizeof(int), compare);

    for (int j = 0; j < i; j++)
        printf("%d", x[j]);

    return 0;
}