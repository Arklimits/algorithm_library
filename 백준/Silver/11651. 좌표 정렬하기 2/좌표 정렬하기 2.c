#include <stdio.h>
#include <stdlib.h>

typedef struct tuple {
  int a;
  int b;
} tuple;

int compare(const tuple *a, const tuple *b) {
  if (a->b == b->b)
    return (a->a - b->a);
  else
    return (a->b - b->b);
}

int main() {
  int n;
  scanf("%d", &n);
  tuple *arr = (tuple *)calloc(n, sizeof(tuple));

  for (int i = 0; i < n; i++) scanf("%d %d", &arr[i].a, &arr[i].b);

  qsort(arr, n, sizeof(tuple), compare);

  for (int i = 0; i < n; i++) printf("%d %d\n", arr[i].a, arr[i].b);

  return 0;
}