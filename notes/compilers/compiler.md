# Compiler

Table of Contents

1. [General Notes](#general-notes)
2. [Interpreters](#interpreters)

## General Notes

Compiler - produces `object code` or `object module`. Object code contains 
instructions / statements in a machine language or intermediary `register 
transfer language`. Object code normally requires services of a `linker`.

Compiler construction touches on topics like:

- Greedy algorithms
- Heuristic search techniques
- Graph algorithms
- Dynamic programming
- Automate theory
- Fixed-point algorithms
- Dynamic memory allocation
- Synchronisation
- Naming
- Locality
- Memory hierarchy management
- Pipeline scheduling

## Interpreters

Interpreters and compilers have a lot in common. However, interpreters emit a
translated program. Emitting a translated program that can be executed to
produce the result. 

## Assembly Generation

- Produces machine-specific assembly code

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

Focuses on dealing with the source code (e.g. Rust, C, C++ etc.). There are a 
number of components that the front end usually has.

- **Lexer / Scanner**
- **Parser**
- **Elaborator**
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

Focuses on dealing with mapping the target language (specifically IR) into the 
instruction set. The back end usually has the following components:

- **(Instruction) Selector** - translates IR into the equivalent target processor ISA.
- **Scheduler** - the execution order of operations must be selected by the _instruction 
scheduling_.
- **Allocator** - the decision about which values should reside in registers at each 
point in the code is done by _register allocation_. 

## Vocabulary

- **symbol** - is name given to any identifier in a program (variable, function, etc).
- **two-phase compiler** - a compiler that consists of a front end and back end.
- **compiler driver** - calls preprocessor, compiler, assembler, linker and converts 
a source file to an executable.
- **parser generator** - a tool that builds a parser from specification
- **S-expression** - symbolic expression, a way to represent data and code in a tree-
like structure, using a notation. S-expression plays a key role in parsing and 
interpreting programs. 

An S-expression typically consists of:
    - Atoms (identifiers, symbols or numbers)
    - Lists (ordered collections of atoms or other lists)

An S-expression represents abstract syntax trees (ASTs). These are pivotal in compilers 
for semantic analysis and generation.

```lisp
;; An s-expression representing the addition of 1 and 2.
;; There are three elements: operator (+) and operands (1 and 2)
(+ 1 2)
```
We can build an equivalent tree out of it:

```
   +
  / \
 1   2
```

Another example of an s-expression:

```lisp
(+ 2 (* 3 4))
```

```
   +
  / \
 2   *
    / \
   3   4
```

- **Execution Context** - an environment or runtime state in which code is evaluated 
and executed. It has all the information needed for the program to run such as 
variable bindings, function declarations, scope and instructions to execute. An 
execution environment typically includes:
    - Variable environment
- **Execution Context** - consists of a heap, a stack, code, and instruction pointer, 
registers etc. 
