 // This File:        my-zip.c
 // Other Files:      my-grep.c my-cat.c my-unzip.c
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
        printf("my-zip: file1 [file2 ...]\n");
        return 1;
    }
    FILE *fp;
    
    int count = 1;
    char curr;
    char next;
    //loop around files
    for (int i = 1; i < argc; i++){
        fp = fopen(argv[i], "r");
        if (fp == NULL) {
            printf("my-zip: cannot open file\n");
            exit(1);
        }
        if (i == 1){ //initialize
            curr = fgetc(fp);
        }
        //char by char
        while((next = fgetc(fp)) != EOF){
            if(next == curr){
                count++;
            }
            else{
                fwrite(&count,4,1,stdout);
                fwrite(&curr,1,1,stdout);
                count = 1;
            }
            curr = next;
        }
        if (i == argc - 1){
            fwrite(&count,4,1,stdout);
            fwrite(&curr,1,1,stdout);
            count = 1;
        }

        fclose(fp);
    }

}

