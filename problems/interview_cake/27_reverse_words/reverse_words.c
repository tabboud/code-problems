#include <stdio.h>
#include <string.h>

void reverse_string(char *string_start, char *string_end) {
    char *start = string_start;
    char *end = string_end;

    while (start < end) {
        char tmp = *start;
        *start++ = *end;
        *end-- = tmp;
    }
}

/* Reverse the order of words in-place
 *
 * Complexity:
 *      Time  -> O(n): Iterate through the array twice
 *      Space -> O(1): In-place reversal
 */
void reverse_words(char *str) {
    // Reverse the entire string, then go through and reverse every word
    char *end = str + strlen(str)-1;
    reverse_string(str, end);

    char *cur = str;
    char *runner = str;

    while (*cur != '\0') {
        // find the spaces and reverse each word
        if (*runner == ' ' || *runner == '\0') {
            reverse_string(cur, runner-1);
            if (*runner == '\0') {
                return;
            }
            cur = runner+1;
        }
        runner++;
    }
}

int main(void) {
    char str[] = "find you will pain only go you recordings security the into if";

    printf("Before: %s\n", str);
    reverse_words(str);
    printf("After: %s\n", str);

    return 0;
}
