# OS

## Process

A process is an instance of a computer programming. A process can be thought of as a program in execution (when the program starts the execution). Early computers supported one process at a time. Modern computers support multiple processes at a time. A computer program can have a number of processes it is associated with and each of these processes might have a number of threads associated with each process.

- file descriptor - each data stream is represented by a file descriptor which
  is a essential a number (unsigned integer). A process needs to record where
  data streams (e.g. standard output) are connected. File descriptors and their
  data streams are stored by the process in a descriptor table (e.g. 0 -
  keyboard, 1 - screen, 3 - network connection). File descriptors do not always
  refer to files, this could be input/output resource (e.g. pipe or socket).
  File descriptors are part of the POSIX API.

### Process states

- New - the process is being created
- Ready - process is waiting to be assigned to a processor (so it can running, executing); a scheduler normally is responsible for this
- Running - instructions are being executed within the process
- Waiting - process is waiting for some event to occur (IO completion, reception of a signal)
- Terminated - process finishes execution (teminates)

- Interrupt - 

### Process Control Block (PCB) aka task control block

Each process in an operating system is represented by a PCB. 

PCB consists of:

- Process ID - unique number or id of a particular process
- Process state - state of a process at a particular moment in time (refer to process state above)
- Program counter - address of the line of the instructions that needs to be executed
- CPU registers - CPU registers that are being used by a particular process (index registers, stack pointers, general purpose registers, etc.)
- CPU scheduling information - pointer to CPU scheduling queue (and other scheduling parameters)
- Memory management information - represents memory that is being used by a particular process.
- Accounting information - keeps track of certain things that are being used by the process (CPU, time, memory, etc.)
- IO information - IO devices that are assigned to a particular process as a process may ned to use IO devices

## Threads

A thread is a basic unit of a process in execution (withing a process). A single process can have from one to many threads. A thread is a basic unit of CPU utilization.

- Threads use the memory of the process they belong to and share memory with other threads

## Program

A program is written is a high level language and converted to binary code for computer to understand by using a compiler (machine code). OS allocated resources and loads the program into the memory and begin its' execution. Once execution starts the program becomes a process.

## Scheduling

There are many processes that are waiting to be executed. Scheduling algorithms determine which process has to be executed first or order in which they have to be executed. Some processes are higher priority than others so they might need to be executed first. 

#### OSes

- illumos - https://illumos.org/
- Process Management (Processes and Threads) - https://www.youtube.com/watch?v=OrM7nZcxXZU&list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O&index=16
- Operating System playlist - https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O
