#include <stdio.h>
#include <stdlib.h>

int compare(const int *a, const int *b){
    return (*a - *b);
}

int main() {
    int n, k;
    int x[10000];

    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%d", &x[i]);

    qsort(x, n, sizeof(int), compare);

    printf("%d\n", x[n-k]);

    return 0;
}