#include <stdio.h>
#include <stdlib.h>

int flag = 0;

typedef struct array {
    int loc;
    int val;
    int comp;
} array;

int compare(const array *a, const array *b) {
    if (!flag)
        return (a->val - b->val);
    else
        return (a->loc - b->loc);
}


int main() {
    int n, i;
    scanf("%d", &n);

    array *arr = (array *) calloc(n, sizeof(array));
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i].val);
        arr[i].loc = i;
    }

    qsort(arr, n, sizeof(array), compare);

    for (i = 1; i < n; i++)
        if (arr[i].val == arr[i - 1].val)
            arr[i].comp = arr[i - 1].comp;
        else
            arr[i].comp = arr[i - 1].comp + 1;

    flag = 1;

    qsort(arr, n, sizeof(array), compare);

    for (i = 0; i < n; i++)
        printf("%d ", arr[i].comp);

    return 0;
}