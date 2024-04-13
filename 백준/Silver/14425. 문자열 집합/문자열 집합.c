#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    return strcmp(*(char **) a, *(char **) b);
}

int binary_search(char **N, const char *comp, const int n) {
    int mid;
    int start = 0, end = n;
    int find;

    if (N == NULL){
        printf("0\n");
        exit(0);
    }

    while (start <= end) {
        mid = (start + end) / 2;
        find = strcmp(N[mid], comp);
        if (find == 0)
            return 1;
        else if (find > 0)
            end = mid - 1;
        else
            start = mid + 1;
    }
    return 0;
}

int main() {
    int n, m, i;
    int cnt = 0;
    scanf("%d %d", &n, &m);

    char **N = calloc(n, sizeof(char *));
    char temp[500];

    for (i = 0; i < n; i++) {
        scanf("%s", temp);
        N[i] = calloc(strlen(temp) + 1, sizeof(char));
        strcpy(N[i], temp);
    }

    qsort(N, n, sizeof(char *), compare);

    for (i = 0; i < m; i++) {
        scanf("%s", temp);
        if (binary_search(N, temp, n - 1))
            cnt++;
    }

    printf("%d\n", cnt);
    free(N);

    return 0;
}