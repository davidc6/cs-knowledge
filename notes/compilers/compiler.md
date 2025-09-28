# Compiler

Table of Contents

1. [General Notes](#general-notes)
2. [Interpreters](#interpreters)

## General Notes

- Compiler - produces `object code` or `object module`. Object code contains
  instructions / statements in a machine language or intermediary `register
  transfer language`. Object code normally requires services of a `linker`.

Compiler construction touches on topics like:

- greedy algorithms
- heuristic search techniques
- graph algorithms
- dynamic programming
- automate theory
- fixed-point algorithms
- dynamic memory allocation
- synchronisation
- naming
- locality
- memory hierarchy management
- pipeline scheduling

## Interpreters

Interpreters and compilers have a lot in common. However, interpreters emit a
translated program. Emitting a translated program that can be executed to
produce the result. 

## Assembly Generation

Produces machine-specific assembly code

## Miscellaneous

- Statement - performs an action but does not produce a value. Not all
  statements are expressions.
- Expression - produces a value
- Compiler needs a driver that calls out to preprocessor, compiler, assembler
  and linker

## Structure

1. Lexer (Tokens)                  -> 
2. Parser (AST)                    -> 
3. Assembly Generator (Assembly)   ->
4. Code Emission (Write to file)   ->

1. Front End - dealing with the source code (e.g. Rust, C, C++ etc.)
    1. Lexer / Scanner
    2. Parser
    3. Elaborator
        - Builds an IR
        - Checking type consistency
        - Laying out storage
2. Optimizer - analysing (IR - intermediate representation) 
    1. Optimisation 1 - to improve the IR, passes over the IR and rewrite it to 
    produce a faster or smaller or more safe (depending on the objective) target 
    program. There can be a number of optimisation stages.
3. Back End - Dealing with the target language 
    - e.g. ISA of CPU
    - e.g. Some human-oriented programming languages
    1. (Instruction) Selector - 
    2. Scheduler - the execution order of operations must be selected by the 
    _instruction scheduling_.
    3. Allocator - the decision about which values should reside in registers at 
    each point in the code is done by _register allocation_. 

## Vocabulary

- **symbol** - is name given to any identifier in a program (variable, function, etc).
- **two-phase compiler** - a compiler that consists of a front end and back end.
- **compiler driver** - calls preprocessor, compiler, assembler, linker and converts 
a source file to an executable.
- **parser generator** - a tool that builds a parser from specification
- **BNF-like grammar** - a formal notation used to describe the syntax of a programming 
language. 

