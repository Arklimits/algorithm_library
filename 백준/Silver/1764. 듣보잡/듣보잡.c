#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    return strcmp(*(char **) a, *(char **) b);
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    char **arr = calloc(n, sizeof(char *));

    for (int i = 0; i < n; i++) {
        arr[i] = calloc(21, sizeof(char));
        scanf("%s", arr[i]);
    }

    qsort(arr, n, sizeof(arr[0]), compare);

    char temp[21];
    int start, end, mid, list = 0, cmp_num;
    char **res = calloc(n, sizeof(char *));
    for (int i = 0; i < m; i++) {
        scanf("%s", temp);
        start = 0, end = n - 1;
        while (start <= end) {
            mid = (start + end) / 2;
            cmp_num = strcmp(arr[mid], temp);
            if (!cmp_num) {
                res[list] = calloc(21, sizeof(char));
                strcpy(res[list++], temp);
                break;
            } else if (cmp_num > 0)
                end = mid - 1;
            else
                start = mid + 1;
        }
    }

    qsort(res, list, sizeof(res[0]), compare);

    printf("%d\n", list);
    for(int i=0;i<list;i++)
        printf("%s\n", res[i]);

    free(arr);
    free(res);

    return 0;
}