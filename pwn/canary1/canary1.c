#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

//gcc -o canary1 canary1.c -no-pie -fno-stack-protector -m32

void vuln(){
        int win = 0;
        int gorfou_y = 0xfcdabdab; //why does people speak of canard_y ?
        char buffer[40];
        puts("Oh, there is a gorfou on the road!");
        fgets(buffer, 60, stdin);
        if (gorfou_y != 0xfcdabdab){
                puts("A car smashed the gorfou :(");
                exit(0);
        }
        if (win){
		setregid(getegid(), getegid());
                system("/bin/sh");
        }
}

void main(){
        vuln();
}

