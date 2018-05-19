 // This File:        my-grep.c
 // Other Files:      my-cat.c my-zip.c my-unzip.c
 // Semester:         CS537 Spring 2018
 // 
 // Author:           Mingyi Lu
 // Email:            mlu69@wisc.edu
 // CS Login:         mlu
 //
 /////////////////////////// OTHER SOURCES OF HELP /////////////////////////////

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char *argv[]) {
    if (argc < 2) {
        printf("my-grep: searchterm [file ...]\n");
        return 1;
    }
    //initialize
    char buffer[100];
    char *line = NULL;
    size_t size = 0;

    if (argc == 2){ //error checking
        while (fgets(buffer, sizeof(buffer), stdin) != NULL){
            if(strstr(buffer, argv[1]) != NULL){
                printf("%s",buffer);
            }
        }
    }
    else {
        FILE *fp;
        for (int i = 2; i < argc; i++){
            fp = fopen(argv[i], "r"); //open file
            if (fp == NULL) {
                printf("my-grep: cannot open file\n");
                exit(1);
            }
            //read line by line
            while (getline(&line, &size,fp) != -1){
                if(strstr(line, argv[1]) != NULL){
                     printf("%s",line);
                }
            }
            fclose(fp);
        }
    }
    return 0;
}
