# Compiler

Table of Contents

1. [General Notes](#general-notes)
2. [Interpreters](#interpreters)

## General Notes

Compiler - produces `object code` or `object module`. Object code contains 
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

1. Lexer (Tokens)
2. Parser (AST)
3. Assembly Generator (Assembly)
4. Code Emission (Write to file)

## Front End

Dealing with the source code (e.g. Rust, C, C++ etc.). There are a number of 
components that the front end usually has.

1. Lexer / Scanner
2. Parser
3. Elaborator
    - Builds an IR
    - Checking type consistency
    - Laying out storage

## Optimizer

An optimizer analyses the IR form of the code and tries to rewrite it to make 
more efficient. Most optimisations consist of analysis and transformation.

Analysing (IR - intermediate representation) - finding where the compiler can 
profitably apply the transformation.

Transforming - rewriting the code into a more efficient form. There have been a 
number of techniques developed to improve the time or space of executable code 
such as loop-invariant code motion.

Optimisations are about improving the IR and rewriting it to produce a faster, 
smaller or safer target program depending on the objective. As a result, there 
can be a number of optimisation stages. 

## Back End

Dealing with the target language 

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

