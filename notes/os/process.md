# Process

A process is an instance of a computer programming. A process can be thought of
as a program in execution (when the program starts the execution). Early
computers supported one process at a time. Modern computers support multiple
processes at a time. A computer program can have a number of processes it is
associated with and each of these processes might have a number of threads
associated with each process.

- Each process gets each own virtual address space
- Virtual address space has a number of well defined areas:
  - **Program code and data.** Code begins at the same fixed address for all
    processes and followed by data locations that corresponds to global C
    variables. There are initialised directly from exec. object file. 
  - **Heap.** This is the next section, which is dynamic in size and expands and
    contracts at run time. Some functions that are responsible for this is C's
    `malloc` and `free`
  - **Stack.** Used to implement function calls.
  - **Shared libraries.** Code for shared libraries such as C's std lib etc are
    located in the middle of the address space. 
  - **Kernel virtual memory.** Address space reserved for kernel, application
    programs not allowed to read or write to this area.

- file descriptor - each data stream is represented by a file descriptor which
  is a essential a number (unsigned integer). A process needs to record where
  data streams (e.g. standard output) are connected. File descriptors and their
  data streams are stored by the process in a descriptor table (e.g. 0 -
  keyboard, 1 - screen, 3 - network connection). File descriptors do not always
  refer to files, this could be input/output resource (e.g. pipe or socket).
  File descriptors are part of the POSIX API.

### Process states

- New - the process is being created
- Ready - process is waiting to be assigned to a processor (so it can running,
  executing); a scheduler normally is responsible for this
- Running - instructions are being executed within the process
- Waiting - process is waiting for some event to occur (IO completion, reception
  of a signal)
- Terminated - process finishes execution (teminates)

- Interrupt - 

### Process Control Block (PCB) aka task control block

Each process in an operating system is represented by a PCB. 

PCB consists of:

- Process ID - unique number or id of a particular process
- Process state - state of a process at a particular moment in time (refer to
  process state above)
- Program counter - address of the line of the instructions that needs to be
  executed
- CPU registers - CPU registers that are being used by a particular process
  (index registers, stack pointers, general purpose registers, etc.)
- CPU scheduling information - pointer to CPU scheduling queue (and other
  scheduling parameters)
- Memory management information - represents memory that is being used by a
  particular process.
- Accounting information - keeps track of certain things that are being used by
  the process (CPU, time, memory, etc.)
- IO information - IO devices that are assigned to a particular process as a
  process may ned to use IO devices

## Threads

A thread is a basic unit of a process in execution (withing a process). A single
process can have from one to many threads. A thread is a basic unit of CPU
utilization.

- Threads use the memory of the process they belong to and share memory with
  other threads

## Program

A program is written is a high level language and converted to binary code for
computer to understand by using a compiler (machine code). OS allocated
resources and loads the program into the memory and begin its' execution. Once
execution starts the program becomes a process.

## Scheduling

There are many processes that are waiting to be executed. Scheduling algorithms
determine which process has to be executed first or order in which they have to
be executed. Some processes are higher priority than others so they might need
to be executed first. 

## Memory

### Stack

- each process gets it's own memory
- parts of memory can be shared between processes
- process can be divided into code and data
- Stack is considered to be data and it's involved in execution of a program
- Stack works like a stack of plates
- Each function gets its own stack frame
- This part of the memory contains address to return to when complete (at minimum), input args, and space for s
- Stack usually starts at a high address in memory and progressively gets lower

### Heap

- Is area of memory that is managed by the process for on the fly memory allocation
- This is for variables whose memory is not known at compile time
- Heap is managed by malloc() (in C) to allocate and free() to free up memory
- Heap is not automatically managed (we allocate/free memory allocated memory)
- Heap is only restricted by the physical size 
- Heap is accessible but any function anywhere in the program
- Heap allocations can be expensive
- Allocating/deallocation memory on heap leads to fragmentation and it makes it
  much harder to efficiently find space for new allocations
- When we find a spot on the heap and allocate memory for it and put value in it
  we get a memory address back and stack stores address of the memory
- Dereferencing a pointer means to access the value on the heap
- Size of the pointer is usually 32 or 63 bits

### Stack vs Heap

- Static (stack) vs dynamic (heap) variable allocation
- Local to functional call, limited in size vs globally accessible, "unlimited in size"
- 

### Virtual memory

It is an abstraction which makes an illusion that each process has access
exclusively to the main memory. Each process has the same view of memory which
is known as virtual address space. Top most address space is reserved for OS
(code and data) and is common to all processes. Lower region is code and data
defined by user's process.

MMU (memory management unit) translates virtual addresses to physical addresses
(using page lookup table). 

### System Call (syscall)

A system call transfers control into the OS while raising the hardware privilege
level. Since user applications run in user mode (a mode where the restrictions  
are set by the hardware to what it can do). This means that an application cannot 
initiate an IO request to disk, send a packet over the wire etc. 

A special hardware instruction called trap usually provides a way to transfer 
control to a trap-handler (that is pre-specified) and raise privilege to kernel 
mode. From there the OS has the full control of the system's hardware.

Once the OS is done with the request, it passes control back to the user via 
return-from-trap (a special instruction), which reverts back to user mode. This 
also passes control back to where the application left off.

Some of most common system calls: read(), write(), open(), close(), fork(), exec()

Both of the following create a child process: 

- fork() - (copy) duplicates the current process.

- exec() - (replace) replaces the current process with a new program, changes the running
program of the current process. All code (text) and data in the process is loss 
and replaced by the executable of the new program. 

A process can become a "zombie" process when terminated but not clean up yet. 
Parent process is responsible for cleaning up children zombie processes. 

If a parent process is idle which child process is running, it can issue a 
wait() syscall which moves it off the ready queue until the termination of the 
child. The parent then waits for the child process to complete with the wait() 
syscall. A process terminates when the final statement is reached. It asks the OS 
to delete it via the exit() system call. All the resources of the process then 
are deallocated and reclaimed by the OS.

#### OSes

- illumos - https://illumos.org/
- Process Management (Processes and Threads) -
  https://www.youtube.com/watch?v=OrM7nZcxXZU&list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O&index=16
- Operating System playlist -
  https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O
- Computer Science from the Bottom Up - https://www.bottomupcs.com/index.xhtml
