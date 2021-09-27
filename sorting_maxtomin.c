#include <stdio.h>

void aplusb();


int main(int argc, char const *argv[])
{
    /* code */
    int a;
    int b;
    a= 9, b=8;

    aplusb(a, b);

    
    return 0;
}

void aplusb( a, b )
{
    int c;
    c=a+b;
    
    printf(c);
}
