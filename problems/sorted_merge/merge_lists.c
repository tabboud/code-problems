#include <stdio.h>
#define SIZE(n) sizeof(n)/sizeof(*n)

/*
 * Merge two sorted lists
 *
 * Complexity:
 *     Time  -> O(m*n): where m is the length of A, and n is length of B
 *     Space -> O(1): No extra space needed
 */
void merge_lists(int *A, int *B, int A_len, int B_len) {
    // get the index of the ends
    int A_end = A_len - 1;
    int B_end = B_len - 1;

    int end = A_len + B_len - 1;

    // Traverse the array comparing the two values and inserting from the end as we go
    while (end > 0) {
        if (A_end >= 0 && B_end >= 0) {
            if (A[A_end] > B[B_end]) {
                A[end] = A[A_end];
                A_end--;
            } else {
                A[end] = B[B_end];
                B_end--;
            }
        } else if (A_end >= 0) {
            // Place the rest of A into A
            while (A_end >= 0) {
                A[end] = A[A_end];
                A_end--;
                end--;
            }
        } else {
            // Place the rest of B into A
            while (B_end > 0) {
                A[end] = B[B_end];
                B_end--;
                end--;
            }
        }
        end--;
    }

    return;
}

void print_list(int *a, int len) {
    for (int i=0; i<len; i++)
        printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int A[10] = {1,2,3,4,5};
    int A_len = SIZE(A);
    int B[5] = {6,7,8,9,10};
    int B_len = SIZE(B);

    print_list(A, A_len); 

    // merge A and B
    merge_lists(A, B, 5, 5);

    print_list(A, A_len); 
}
