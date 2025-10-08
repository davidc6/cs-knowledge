# Parsers

## Parser

- Converts tokens into an AST (abstract syntax tree). This represents the
  program in a way it can be easily traversed and analysed.
- It can be hand-written or a parser-generator (such as Bison or ANTLR) can be 
used.
- **Parser Generator** - takes a formal grammar (like EBNF) as input and generates parsing 
  code automatically. Parser generators prioritise performance and static checks. Example are ANTLR, Happy.
- **Parser Combinator** - is a library where parsers are built by composing smaller parsing 
functions (known as combinators) that operate directly on input streams. Parser are then written as as normal code. Parser combinators prioritise flexibility and ease of use. Example are Nom.
- Tree data structures are a natural way to represent the hierarchical relationship.
The parser generates an AST (abstract syntax tree) from the list of tokens.
- AST descriptions are done in a AST language like ASDL (Zephyr Abstract Syntax 
Description Language).
- Visitor pattern is used when working with ASTs after parsing. The main purpose is to separate operations (type checking, interpretation, code generation) from the object structure.
  - Each tree node accepts a visitor object.
  - Visitor class implements `visit` method for each node type.
  - When `accept` is called on the node, corresponding visitor method is called for the type.
  - This allows adding new operations without modifying the AST node class, just new visitor implementation.
Backtracking - 

```
// Pseudo language
int main(void) {
    return 2;
}
```

```
// ASDL notation
program = Program(function_definition)
// Function('main', body)
function_definition = Function(identifier name, statement body)
// body
statement = Return(exp)
// Constant(2)
exp = Constant(int)
```

- Parsing expression - a kind of pattern that each string may either match or 
not match

### PEG

PEG stands for Parsing Expression Grammar. PEGs are similar to CFGs but the choice 
operator is ordered and not ambiguous.

CFG grammar is non-deterministic. An input could result in one or more possible 
parse-trees. Generally, CFG-based parser generators restrict determinability of 
the grammar.


Ordered choice - 

It is:
    - A way of specifying formal languages for text processing
	- Can be used for matching (regex) or building recursive descent parsers 
    (lex/yacc)
	- Closely related to top-down parsing
	- Example projects: Antlr
	- If we to parse (0.123, -.987, 2.4, 3)
        - TODO
	- PEG is almost identical to a grammar in EBNF
	- Resources:
        - https://berthub.eu/articles/posts/practical-peg-parsing/

## Grammar

**Grammar** - grammars serve as a means of specification in programming languages. It is a 
general way to describe a language. 

**Non-terminal Symbols** - are replaced using productions until we arrive at a sentence. These are 
not "fixed" or variables. These do not terminate the process.

**Terminal Symbols** - these terminate the process of generation. Sometimes these are also called 
constants. 

**Terminal Symbol** - inside the compiler terminal symbols are usually lexical tokens. 

**(N, T, P, S)** - formal grammars are defined by 4 tuples: non-terminals, terminals, productions, 
S symbol (starts the derivation of sentences).
  - N is a finite, non-empty set of Non-terminals
  - T is a finite, non-empty set of Terminals
  - N (union) T = (phi)
  - S is a special non-terminal called Start symbol
  - P is a finite set Production Rules of the form (a->b)

**Metalanguage** - is used to describe a context-free grammar. 
A metalanguage is a form of specialised language that is used to describe another 
(programming) language. It provides syntax, rules and structure for that language. 
Metalanguages are crucial for compiler construction.

**Context-free grammar (CFG)** - is an important class of grammars used to describe a programming 
language syntax using a powerful notation. Traditionally, CFG has been used for this. Grammars often 
contain recursive rules. These rules explain how valid sentences or structures can be 
formed in a programming language. In compilers these are used to define how code looks 
and what patterns are allowed. There tools to describe CFGs.

**BNF** - is the notation to represent a CFG. Each BNF rule is called a production. 


