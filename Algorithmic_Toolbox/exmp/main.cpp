#include <stdio.h>

unsigned int f(unsigned int n) {

if(n == 0) return 1;

else if(n == 1) return 1;

return f(n-2) + f(n-1);

}

int main(int argc, char **argv) {
unsigned int n;
scanf(n);
n = f(n);
printf("f(n) = %u\n", n);

return 0;

}
