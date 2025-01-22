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

L0 - Registers
L1 - holds tens of thousands of bytes and nearly as fast as the registers
L2 - larger cache, hundreds of thousands to millions of bytes, connected to the processor by special bus and 5 times longer for processor to access
but 5 to 10 times faster than accessing the main memory
L1 & L2 - are implemented using *SRAM* (static random access memory)
L3 - some more powerful systems have this level too. 

Cache lines - chunks of memory handled by cache are called cache lines. It is a block of data of fixed size that gets transferred between memory and cache. 

Set - 

Block - 

Locality - tendency to access data and code in localized regions. By setting up caches to hold data that is frequently accessed, most memory operations can be performed using the fast caches. 

L4 - (*DRAM*) main memory
L5 - local disk
L6 - remote storage


