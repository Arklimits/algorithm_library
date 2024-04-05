#include <stdio.h>

int main() {
    int left[3], right[3];
    int res_left, res_right;
    int i;

    for (i = 0; i < 3; i++) {
        scanf("%d %d", &left[i], &right[i]);
    }

    if (left[0] == left[1]) res_left = left[2];
    else if (left[0] == left[2]) res_left = left[1];
    else res_left = left[0];

    if (right[0] == right[1]) res_right = right[2];
    else if (right[0] == right[2]) res_right = right[1];
    else res_right = right[0];

    printf("%d %d\n", res_left, res_right);

    return 0;
}