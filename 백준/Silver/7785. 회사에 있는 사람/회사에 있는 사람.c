#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct list_t {
    char name[6];
    char status[6];
} list_t;

int compare(const list_t *a, const list_t *b) {
    return strcmp(b->name, a->name);
}

int main() {
    int n, i, new = 0;
    int j;

    scanf("%d", &n);

    list_t list[n];

    for (i = 0; i < n; i++)
        scanf("%s %s", list[i].name, list[i].status);

    qsort(list, n, sizeof(list_t), compare);

    for (i = 0; i < n; i++) {
        if (!strcmp(list[i].name, list[i + 1].name))
            i++;
        else
            printf("%s\n", list[i].name);
    }

    return 0;

}