#pragma clang diagnostic ignored "-Wincompatible-function-pointer-types"
#pragma ide diagnostic ignored "cert-err34-c"

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *nextNode;
};

struct Stack {
    struct Node *top;
};

void init(struct Stack *s) {
    s->top = NULL;
}

int is_empty(struct Stack *s) {
    return (s->top == NULL);
}

void push(struct Stack *s, int data) {
    struct Node *temp = (struct Node *) malloc(sizeof(struct Node));

    temp->data = data;
    temp->nextNode = s->top;
    s->top = temp;
}

int pop(struct Stack *s) {
    if (is_empty(s)) {
        return -1;
    }
    else {
        struct Node *temp = s->top;
        int data = temp->data;

        s->top = s->top->nextNode;

        free(temp);
        temp = NULL;

        return data;
    }
}

//int length(struct Stack *s) { // --- 삭제한 부분 ---
//    int count = 0;
//    for (struct Node *p = s->top; p != NULL; p = p->nextNode) {
//        count++;
//    }
//
//    return count;
//}

//void print_stack(struct Stack *s)
//{
//    printf("Test :");
//    for(struct Node *p = s->top; p!=NULL;p = p->nextNode)
//        printf("%d-> ",p->data);
//    printf("NULL \n");
//}

int main() {
    int n, i, c, v, size;
    struct Stack stack;
    init(&stack);
    size = 0;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &c);

        switch (c) {
            case 1:
                scanf("%d", &v);
                push(&stack, v);
                size++;
                break;
            case 2:
                printf("%d\n", pop(&stack));
                if (size > 0) size--;
                break;
            case 3:
                printf("%d\n", size);
                break;
            case 4:
                printf("%d\n", is_empty(&stack));
                break;
            case 5:
                if (is_empty(&stack)) printf("-1\n");
                else printf("%d\n", stack.top->data);
                break;
            default:
                exit(-1);
        }
    }

    return 0;
}
