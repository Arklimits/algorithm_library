#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *) a - *(int *) b);
}

int bisearch(int n, int *arr, int b) {
    int start = 0, end = n - 1;
    int mid;

    while (start <= end) {
        mid = (start + end) / 2;
        if (arr[mid] == b)
            return 1;
        else if (arr[mid] > b)
            end = mid - 1;
        else
            start = mid + 1;
    }
    return 0;
}

int main() {
    int n, m;
    int res = 0;
    scanf("%d %d", &n, &m);

    int *A = calloc(n, sizeof(int));

    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
        res++;
    }

    qsort(A, n, sizeof(int), compare);

    int temp;
    for (int i = 0; i < m; i++) {
        scanf("%d", &temp);

        if (bisearch(n, A, temp))
            res--;
        else
            res++;
    }

    printf("%d\n", res);

    free(A);

    return 0;
}