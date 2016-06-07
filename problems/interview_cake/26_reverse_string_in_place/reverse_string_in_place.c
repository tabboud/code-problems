#include <stdio.h>
#include <string.h>

/* Reverse a string in-place
 *
 * Complexity:
 *      Time  -> O(n): Iterate through the array once
 *      Space -> O(1): In-place reversal
 */
void reverse_string(char *string) {
    /* Array vs pointer arithmetic
    int end = strlen(string) - 1;
    
    for (int start=0; start < end; start++, end--) {
        char tmp = string[start];
        string[start] = string[end];
        string[end] = tmp;
    }
    */

    char *start = string;
    char *end = string + strlen(string) - 1;

    while (start < end) {
        char tmp = *start;
        *start++ = *end;
        *end-- = tmp;
    }
}

int main(void) {
    char str[] = "Toxny";

    printf("Before: %s\n", str);
    reverse_string(str);
    printf("After: %s\n", str);

    return 0;
}
