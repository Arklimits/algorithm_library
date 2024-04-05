#include <stdio.h>
#include <stdlib.h>

int compare(const int *a, const int *b) {
    return (*a - *b);
}



int main() {
    int arr[3];
    int i;
    while (1) {
        for (i = 0; i < 3; i++) scanf("%d", &arr[i]);

        if (arr[0] == 0) break;

        qsort(arr, 3, sizeof(int), compare);

        if (arr[2] >= arr[0] + arr[1]) printf("Invalid\n");
        else if (arr[0] == arr[2]) printf("Equilateral\n");
        else if (arr[0] == arr[1] || arr[1] == arr[2]) printf("Isosceles\n");
        else printf("Scalene\n");
    }


    return 0;
}