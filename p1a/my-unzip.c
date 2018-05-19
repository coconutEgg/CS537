 // This File:        my-unzip.c
 // Other Files:      my-grep.c my-zip.c my-cat.c
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
        printf("my-unzip: file1 [file2 ...]\n");
        return 1;
    }
    FILE *fp;
    char character;
    int num;
    for (int i = 1; i < argc; i++) {
        fp = fopen(argv[1], "r");
        while(fread(&num, 4, 1, fp) == 1){

            if(fread(&character, 1, 1,fp) == 1){
                for (int j = 0; j < num; j++) {
                    printf("%c", character);
                }
            }
            else 
                break;

        }
        fclose(fp);
    }
}

