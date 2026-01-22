# Async

- The difference between async and multithreading is that async is managed entirely 
within the program without any help from the OS. A sequence of executions in async 
is called a task (sometimes also called a green-thread).

- An async system has a scheduler which coordinates order of tasks. 

- An async IO means that a program is free to complete its' task while some IO 
takes place.

- Threads do IO from the OS (OS-native)
    - OS pauses threads
    - threads get work done
    - OS wakes up threads
    - Preemptive multitasking

- Async (non OS-native)
     - Task requires IO from the (user-space) runtime
     - Runtime requests IO from the OS
     - OS returns control to the runtime
     - Overheads are lower (given green threads)
     - Cooperative multitasking where tasks voluntarily give control back to 
     the runtime
     - Buggy task can run for a long time and block thus slowing or blocking the 
     system 

- Some programs use both (threads and async)
    - DB uses async to manage network communication with the clients
    - Data computations are managed by the threads

## Rust-specific Async

- Future
    - A value that might not be available yet (a file being downloaded, a result 
    of a computation by another task, etc.)
    -  
