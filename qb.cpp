
#include <stdio.h>

int main() {
    int num = 0;
    int den = 0;

    scanf("%d %d", &num, &den);

    int numDivides = 0;
    while (num % 2 == 0 && den % 2 == 0) {
        numDivides++;
        num /= 2;
        den /= 2;
    }

    if (num % 2 == 1 && den % 2 == 1) {
        1 << numDivides;
    }

    return 0;
}
