#include <stdio.h>
int gcd(int a, int b) {
    return b ? gcd(b, a%b) : a;
}

int main() {
    int t, a, b;
    scanf("%d", &t);
    while (t--){
        scanf("%d %d", &a, &b);
        printf("%d\n", a*b / gcd(a, b));
    }
}
