 // This File:        my-cat.c
 // Other Files:      my-grep.c my-zip.c my-unzip.c
 // Semester:         CS537 Spring 2018
 // 
 // Author:           Mingyi Lu
 // Email:            mlu69@wisc.edu
 // CS Login:         mlu
 //
 /////////////////////////// OTHER SOURCES OF HELP /////////////////////////////
 
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]) {
    if (argc < 1) {
        return 1;
    }
    FILE *fp;
    char buffer[100]; //initialize buffer
    
    //begin reading
    for (int i = 1; i < argc; i++){
        fp = fopen(argv[i], "r"); //open file
        if (fp == NULL) { //error checking
            printf("my-cat: cannot open file\n");
            exit(1);
        }
        while (fgets(buffer, sizeof(buffer), fp) != NULL){
            printf("%s", buffer);
        }
        fclose(fp);
    }

    return 0;
}
