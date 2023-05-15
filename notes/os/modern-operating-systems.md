# Modern Operating Systems

## Components

- A modern computer can be abstracted into CPU, memory and I/O devices and all
  connected via a system bus to communicate with each other
- CPU fetches instructions from memory and executes them
- Basic cycle of every CPU is to fetch the 1st instruction from memory, decode
  it (determine type and operands, execute it and repeat until program finishes).
- Each CPU has a specific set of instructions it executes, e.g. x86 processor
  cannot execute ARM instructions (program) and vice versa
- Accessing memory to get instruction or dta word takes longer than executing it
- CPU contain registers inside to hold key variables and temporary results
- A register is a type of memory inside of a CPU and is used for data that gets
  shifted to and from the memory
- Is it quicker to move data to and from registers than RAM or cache hence it
  speeds up processing time
- An instruction is a single command a CPU can process
- Instructions are bit strings (sequence of 0s and 1s)
- Opcode - a unique binary number representing operation to be performed
- Operand(s) - reference/pointer to data needed for operation (register number,
  memory address, secondary storage or I/O device)
- Instruction Set Architecture (ISA) / computer architecture - abstract model of
  of a computer. A device that executes instructions described by that ISA (e.g.
  CPU), is an implementation. 
- Computer architecture is a set of rules and methods that describe the
  functionality, organization and implementation of a computer system
- Reduced instruction set computer (RISC) - 
- Execution per unit time (throughput) - number of executions per unit of time
