/*
Test of the Raspberry Pi pico C/C++ SDK
By Samples & Tests
16 May 2022
# Ver 0.1

*/

#include <stdio.h>
#include "pico/stdlib.h"


int main()
{
int testint;
    stdio_init_all();
	while(true){
    		puts("Hello, world!");
		puts("press any key");
		testint = getchar();
		

	}


    return 0;
}
