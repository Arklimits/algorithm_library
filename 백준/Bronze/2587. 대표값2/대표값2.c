#include <stdio.h>
#include <stdlib.h>

int compare(const int *a, const int *b){
    return (*a - *b);
}

int main(){
    int arr[5], sum = 0;

    for (int i=0;i<5;i++){
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    qsort(arr, 5,sizeof(int),compare);

    printf("%d\n%d\n", sum/5, arr[2]);

    return 0;
}