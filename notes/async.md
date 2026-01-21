# Async

- The difference between async and multithreading is that async is managed entirely 
within the program without any help from the OS. A sequence of executions in async 
is called a task (sometimes also called a green-thread).

- An async system has a scheduler which coordinates order of tasks. 

- An async IO means that a program is free to complete its' task while some IO 
takes place.

- Threads do IO from the OS. 
    - OS pauses threads
    - threads get work done
    - OS wakes up threads

- Async
     - Task requires IO from the runtime
     - Runtime requests IO from the OS
     - OS returns control to the runtime
