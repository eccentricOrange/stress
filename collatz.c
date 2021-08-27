#include <stdio.h>

unsigned long long int collatz(unsigned long long int valIn);

int main(void) {
    unsigned long long int valOut;
    for (unsigned long long int i = 1000000; i > 1; i--) {
        // printf("\n%lld\n", i);
        valOut = collatz(i);
    }
}

unsigned long long int collatz(unsigned long long int valIn) {
    if (valIn == 1) {
        return 1;
    }

    // printf("%lld\n", valIn);
    return collatz(((((3 * valIn) + 1) * (valIn % 2)) + ((valIn / 2) * ((valIn + 1) % 2))));
}