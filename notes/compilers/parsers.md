# Parsers

## Parser

- Converts tokens into an AST (abstract syntax tree). This represents the
  program in a way it can be easily traversed and analysed.
- It can be hand-written or a parser-generator (such as Bison or ANTLR) can be 
used.
- Tree data structures are a natural way to represent the hierarchical relationship.
The parser generates an AST (abstract syntax tree) from the list of tokens.
- AST descriptions are done in a AST language like ASDL (Zephyr Abstract Syntax 
Description Language).

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

PEG stands for parsing expression grammar. It is:
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

**Metalanguage** - is used to describe a context-free grammar. 
A metalanguage is a form of specialised language that is used to describe another 
(programming) language. It provides syntax, rules and structure for that language. 
Metalanguages are crucial for compiler construction.

**Context-free grammar (CFG)**- to describe a programming language syntax we need a 
powerful notation. Traditionally, CFG has been used for this. Grammars often contain 
recursive rules. Each

**BNF** - is the notation to represent a CFG. Each BNF rule is called a production. 


