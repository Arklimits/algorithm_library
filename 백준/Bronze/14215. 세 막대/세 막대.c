#include <stdio.h>
#include <stdlib.h>

int compare(const int *a, const int *b) {
    return (*a - *b);
}


int main() {
    int arr[3];
    int i;

    for (i = 0; i < 3; i++) scanf("%d", &arr[i]);

    qsort(arr, 3, sizeof(int), compare);

    if (arr[2] >= arr[1] + arr[0]) arr[2] = arr[1] + arr[0] - 1;

    printf("%d\n", arr[0] + arr[1] + arr[2]);
}
