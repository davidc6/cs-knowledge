# Scanner

## Lexer / Lexical Analyser / Scanner / Tokeniser

Sometimes also referred to as a scanner. Sometimes scanner is also mentioned as
the initial stage of lexer. A lexer tokenises (breaks the code up into tokens)
the source code.

- A lexer brakes the code up into tokens
- A token is a smallest unit of a program. It can be a delimiter, keyword,
  identifier, arithmetic symbol, etc.
- Scanners are based on recognisers that simulate deterministic finite automata

### Lexical Analysis

#### Finite Automata

It is a computational model that is used to recognise patterns within input
data (input sequence). This is mostly in lexical analysis, text processing and
regular expression matching.

- Finite automaton (aka finite-state machine) is a mathematical model of
  computation that represents a system with a finite number of states, an
  alphabet, a transition function, a start state and one of more accepting
  states. 

## Recogniser

These are programs that identify words in a stream of characters. 

## NFA (Nondeterministic finite automaton)

- Intermediate step from regex to DFA (deterministic finite automaton)
- Uses a set on NFAs one per token type to scan input
- Each regex converted to an NFA
- 

