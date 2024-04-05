#include <stdio.h>

int main() {
    int n, i;
    int x_max, x_min, y_max, y_min;
    int x, y;

    scanf("%d", &n);
    scanf("%d %d", &x_max, &y_max);

    x_min = x_max;
    y_min = y_max;

    for (i = 1; i < n; i++) {
        scanf("%d %d", &x, &y);

        if (x > x_max) x_max = x;
        else if (x < x_min) x_min = x;
        if (y > y_max) y_max = y;
        else if (y < y_min) y_min = y;
    }

    printf("%d\n", (x_max - x_min) * (y_max - y_min));

    return 0;
}