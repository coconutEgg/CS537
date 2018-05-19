#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <assert.h>
#include <string.h>
#include <stdbool.h>
#include <sys/mman.h>
#include <unistd.h>
#include <math.h>
#include "fs.h"
#define ROOTINO 1
#define BSIZE 512
#define IPB           (BSIZE / sizeof(struct dinode))
#define IBLOCK(i)     ((i) / IPB + 2)
#define BPB           (BSIZE*8)
#define BBLOCK(b, ninodes) (b/BPB + (ninodes)/IPB + 3)
#define T_DIR  1
#define T_FILE 2
#define T_DEV  3
#define NDIRECT 12
#define NINDIRECT (512 / sizeof(uint))
#define MAXFILE (12 + NINDIRECT)
#define DIR_SIZE 14
typedef unsigned int   uint;
typedef unsigned short ushort;
typedef unsigned char  uchar;
struct superblock {
  uint size;         // Size of file system image (blocks)
  uint nblocks;      // Number of data blocks
  uint ninodes;      // Number of inodes.
};
struct dinode {
  short type;           // File type
  short major;          // Major device number (T_DEV only)
  short minor;          // Minor device number (T_DEV only)
  short nlink;          // Number of links to inode in file system
  uint size;            // Size of file (bytes)
  uint addrs[NDIRECT+1];   // Data block addresses
};
struct dirent {
  ushort inum;
  char name[DIRSIZ];
};
fprintf(stderr,"ERROR: bad inode.\n");
fprintf(stderr,"ERROR: bad direct address in inode.\n");
fprintf(stderr,"ERROR: bad indirect address in inode.\n");
fprintf(stderr,"ERROR: root directory does not exist.\n");
fprintf(stderr,"ERROR: directory not properly formatted.\n");
fprintf(stderr,"ERROR: address used by inode but marked free in bitmap.\n");
fprintf(stderr,"ERROR: bitmap marks block in use but it is not in use.\n");
fprintf(stderr,"ERROR: direct address used more than once.\n");
fprintf(stderr,"ERROR: indirect address used more than once.\n");
fprintf(stderr,"ERROR: inode marked use but not found in a directory.\n");
fprintf(stderr,"ERROR: inode referred to in directory but marked free.\n");
fprintf(stderr,"ERROR: bad reference count for file.\n");
fprintf(stderr,"ERROR: directory appears more than once in file system.\n");
fprintf(stderr,"ERROR: parent directory mismatch.\n");
fprintf(stderr,"ERROR: inaccessible directory exists.\n");
int main(int argc, char *argv[]){
	if (argc == 1){
		fprintf(stderr, "Usage: xcheck <file_system_image>\n");
		exit(1);
	}
	int fd = open(argv[1], O_RDONLY);
	if (fd < 0){
        fprintf(stderr, "image not found.\n");
		exit(1);
    }
	struct stat file_stat;
    fstat(fd, &file_stat);
    size_t fsize = file_stat.st_size;
	void* img = mmap(NULL, fsize, PROT_READ, MAP_SHARED, fd, 0);
	struct superblock *sb = (struct superblock *)(img + BSIZE);
    uint size = sb->size;
    uint ninodes = sb->ninodes;
    uint nblocks = sb->nblocks;
	if (inode->type == 0)
	{}
	if (strcmp(dir->name,".") != 0)
	{}
	if (strcmp(dir->name,"..") != 0)
	{}
	munmap(img, fsize);
	exit(0);
}
