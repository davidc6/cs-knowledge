# Memory

## Q & A

- **Q:** What is volatile memory?
- **A:** Memory that is not permanent and everything stored in it will be lost once the system shuts down. It requires constant power supply to maintain stored data.
---
- **Q:** Why is cache memory important?
- **A:** It speeds up data retrieval since the data in cache is usually stored in a location that is quicker (than RAM or storage) for CPU to access frequently used data and instructions. 
---
- **Q:** What is virtual memory?
- **A:** It is a technique used by the operating system to create an illusion for the processes that they have unlimited and access to computer's memory.  It is used as a layer between the physical memory and processes in order to manage memory effectively, enable data in RAM and transfer not currently used data to secondary storage. When there's no more RAM available, the data gets stored on the secondary drive. Memory management unit (MMU) will swap the least used data out of RAM and into a virtual memory. Virtual memory allows files and memory to be shared by two or more processes through *page sharing*.
    - For example, standard C library (libc) can be shared by several processes through mapping of the shared object (.so) into a virtual address space. 
    - Two or more processes can communicate through the use of shared memory. Virtual memory allows a process to create a region of memory that it can share with another process.
    - Pages can be shared during process creation with *fork()* system call which speeds up process creation.
---
- **Q:** What is virtual address space?
- **A:** Virtual view of how the process is stored in memory. MMU maps logical/virtual pages to physical frames in memory. Physical page frames assigned to a process may not be contiguous. 