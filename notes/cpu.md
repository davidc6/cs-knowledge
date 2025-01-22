# Processor

CPU (Central Processing Unit) - interprets instructors stores in main memory. Essentially, it's a word-size storage device called program counter (PC). PC contains address of some machine-language instruction in main-memory.

Instruction set architecture - defines how a processor operates on this very simple instruction execution model.

The processor reads the instruction from memory pointed at by the PC, interprets the bits, performs simple operations and updates PC to point to next instruction. 

Instructions revolve around main memory, the register file (small storage that consists of word-size registers) and ALU. 

Example of such operations:

- Load: copy a byte/word from main memory into a register
- Store: copy a byte/word from a register to a location in main memory
- Operate
    - copy the contents of two registers to ALU
    - perform arithmetic operation on the words
    - store results in a register
- Jump: extract a word from the instruction and copy the word into the program counter (PC)

All of the these overwrites previous contents.

CPU components
    - PC (Program Counter)
    - Register file (array of processors registers)
    - ALU (Arithmetic Logic Unit)
    - Bus Interface (the mechanism by which CPU communicates with memory and devices)

Because processors run faster than memory, small, faster storage devices called cache memories are used inside the CPU. The main idean is that one level serves as cache for level below it. There are different levels of caches:

## Cache

L0 (~1 kb) - Registers
L1 (~256 kb) - holds tens of thousands of bytes and nearly as fast as the registers (2kb to 64kb)
L2 (~1 mb) - larger cache, hundreds of thousands to millions of bytes, connected to the processor by special bus and 5 times longer for processor to access
but 5 to 10 times faster than accessing the main memory
L1 & L2 - are implemented using *SRAM* (static random access memory)
L3 (~8 mb) - some more powerful systems have this level too. This is shared between CPUs.
L4 (128 mb) - still quite uncommon and is generally (DRAM), 

Cache lines - chunks of memory handled by cache are called cache lines. It is a block of data of fixed size that gets transferred between memory and cache. 
Cache miss - 

Set - a row in the cache. The number of blocks per set is determined by the layout of cache (direct mapped, set-associative, or fully associative)

Block - the basic unit for cache storage, may contain multiple bytes/words of data.

Locality - tendency to access data and code in localized regions. By setting up caches to hold data that is frequently accessed, most memory operations can be performed using the fast caches. 

L4 - (**DRAM**) main memory
L5 - local disk
    - How is memory laid out in pages, page fault (page does exist in RAM). Dirty bit is whether that page was touched and used. Cache eviction (LRU) 

L6 - remote storage

### Resources

- [The Basics of Cache](https://cseweb.ucsd.edu/classes/su07/cse141/cache-handout.pdf)

A single CPU can execute multiple processes concurrently by having a processor switch among them. The interleaving is performed by the OS using a mechanism known as **context switching**.

Virtual to physical page translations - 
Providing an elusion 

Every process has it's own virtual memory mapping. Two processes might have the same virtual address mapped to different physical space 

OS keeps track of all the state information that the process needs in order to run. This state is known as the context. 

Virtual - 
Physical memory - 
Page table - 
Walking the page table - 
