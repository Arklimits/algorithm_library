#include <stdio.h>
#include <math.h>

int main() {
    int n, i;
    int x1, y1, r1, x2, y2, r2;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        float d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
        float p = r1 + r2;
        float s = r1 > r2 ? r1 - r2 : r2 - r1;

        if(d == 0 && r1 == r2) printf("-1\n");
        else if(d < p && s < d) printf("2\n");
        else if(d == p || d == s) printf("1\n");
        else printf("0\n");
    }

    return 0;
}