#include <stdio.h>
#include <stdlib.h>

void dfs(int n, int m, int i, int d, int *arr) {
    if (d == m) {
        for (int j = 0; j < m; j++)
            printf("%d ", arr[j]);
        printf("\n");

        return;
    }

    for (int j = i + 1; j <= n; j++) {
        arr[d] = j;
        dfs(n, m, j, d + 1, arr);
    }
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int *arr = calloc(n, sizeof(int));

    for (int i = 1; i <= n - m + 1; i++) {
        arr[0] = i;
        dfs(n, m, i, 1, arr);
    }

    free(arr);
    
    return 0;
}