# CS 537 p4b

Author: Mingyi Lu, Jason Jiang

## purpose

1. new system call: clone(), join()
2. use clone() to build a little thread library: thread_create(), lock_acquire(), lock_release()



## clone()

int clone(void(*fcn)(void *, void *), void *arg1, void *arg2, void *stack)

创建一个新的线程，共享了进程的地址空间

file descriptors的复制参考fork()

stack一页大小 page-aligned

fcn用来定位线程开始执行的地址

线程的PID会返回给parent，每一个线程有自己的PID

只exit(),不要return



## join()

int join(void **stack)

等待一个子线程的exit

返回等待的子线程的PID

线程的stack复制进这个argument stack里



## other

`int wait()` should wait for a child process that does not share the address space with this process. It should also free the address space if this is last reference to it. Also, `exit()` should work as before but for both processes and threads; little change is required here.



## TODO

1. kernel/syscall.c add clone() and join() two system calls
2. kernel/sysfunc.h add clone() and join()
3. user/user.h add clone() and join()
4. user/usys.S add clone() and join()
5. Include/syscall.h add clone() and join()


6. kernel/sysproc.c add clone() and join()
7. kernel/proc.c implement clone()