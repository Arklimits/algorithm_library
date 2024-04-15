#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct pokemon_t {
    int number;
    char pokemon[21];
} pokemon_t;

int compare(const pokemon_t *a, const pokemon_t *b) {
    return strcmp(a->pokemon, b->pokemon);
}

int main() {
    int n, m, i;
    char find[21];
    scanf("%d %d", &n, &m);

    pokemon_t list[n];

    for (i = 0; i < n; i++) {
        scanf("%s", list[i].pokemon);
        list[i].number = i + 1;
    }

    pokemon_t ordered_list[n];
    memcpy(&ordered_list, &list, n * sizeof(pokemon_t));
    qsort(ordered_list, n, sizeof(pokemon_t), compare);

    int j, num, ten;
    int start, end, mid;
    int cmpnum;
    for (i = 0; i < m; i++) {
        scanf("%s", find);
        if (find[0] >= '0' && find[0] <= '9') {
            num = 0, ten = 1;
            
            for (j = strlen(find) - 1; j >= 0; --j) {
                num += (find[j] - '0') * ten;
                ten *= 10;
            }
            printf("%s\n", list[num - 1].pokemon);
            
        } else {
            start = 0, end = n;
            while (start <= end) {
                mid = (start + end) / 2;
                cmpnum = strcmp(find, ordered_list[mid].pokemon);
                
                if (!cmpnum) {
                    printf("%d\n", ordered_list[mid].number);
                    break;
                    
                } else if (cmpnum < 0)
                    end = mid - 1;
                
                else
                    start = mid + 1;
            }
        }
    }

    return 0;
}