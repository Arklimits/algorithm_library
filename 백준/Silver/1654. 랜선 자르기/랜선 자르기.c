#include <stdio.h>

int main() {
    int k, n, i;
    long end = 0;

    scanf("%d %d", &k, &n);
    long arr[k];

    for (i = 0; i < k; i++) {
        scanf("%ld", &arr[i]);
        end += arr[i];
    }
    end /= n;
    long start = 1, mid = 0, val = 0;
    long res = 0;
    while (start <= end) {
        mid = (start + end) / 2;
        val = 0;
        for (i = 0; i < k; i++)
            val += arr[i] / mid;

        if (val >= n) {
            res = mid;
            start = mid + 1;
        } else
            end = mid - 1;
    }

    printf("%ld\n", res);

    return 0;
}