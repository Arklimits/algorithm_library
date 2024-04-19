#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, m, temp;
    scanf("%d %d", &n, &m);

    int *arr = calloc(n, sizeof(int));

    scanf("%d", &arr[0]);

    for (int j = 0; j < n - 1; j++) {
        scanf("%d", &temp);
        arr[j + 1] = arr[j] + temp;
    }

    int start, end;
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &start, &end);
        if (start == 1)
            printf("%d\n", arr[end - 1]);
        else
            printf("%d\n", arr[end - 1] - arr[start - 2]);
    }

    free(arr);

    return 0;
}