# Data structures

## Abstract data type

- ADT is defined by behaviour (operations) and not concrete implementation. In other words, it is an implementation-independent representation of how data is organised.
- Common ADTs: stack, queue, priority queue, dictionary

## Abstract data type structure

- ADTS is the actual structure of data used to store data
- Common data structures that are used to implement data types: array, linked list, hash table, tree(s)

## Array

- An allocated block of memory that stores data of the same data type. For example, an array of 4 integers.

## Tuple

- An ordered group of elements (or items) that make a single (compound) structure
- Tuples can container multiple types and are used to group elements together
- This data structure is immutable hence cannot be modified and order is guaranteed
- Elements are accessed by index
- In functional programming tuples are implement as [`product types`](/notes/programming-languages.md#product-types)
-

```python
thisistuple = ("one", "two", "three")
```
- JavaScript tuple proposal - https://github.com/tc39/proposal-record-tuple



## List

- List is similar to an array but allows elements of various types. A list can store heterogeneous data.
- It is growable, meaning it can dynamically expand if necessary
- Lists support such operations as `get()`, `insert()`, `remove()`, `removeAt()`, etc.

## Linked list

- Linked list allows to store data anywhere in the memory
- Each node in a linked list stores some data and the address to the next node
  - Singly - 
  - Doubly - 
  - Circularly - 

## Trie (prefix tree, digital tree)

- Trie (derives from word retrieval) data structure is a very useful data structure when working with strings. Every tree leaf represents one string. Each node is exactly one character of the string. 
- Trie data structure is useful when looking for a string is a set of strings. This data structure is simple to build and search but can be expensive on memory.

```
-age // suffix; meaning - a result
storage // word
```

![Trie](/assets/trie-data-structure.png?raw=true "Optional")

### Resources

- Tries (Prefix Trees) - https://www.baeldung.com/cs/tries-prefix-trees
- Trie vizualization - https://www.cs.usfca.edu/~galles/visualization/Trie.html
- Trie data structure from scratch - https://simpledevcode.wordpress.com/2018/12/04/trie-data-structure-from-scratch/

## Suffix tree

- Suffix tree is a form of a trie data structure that prepares strings for fast pattern matching operations. It contains i suffixes of i-character string.
- Build a suffix tree - https://www.youtube.com/watch?v=qh2leThTv0Y

## Dynamic programming

DP is an algorithm design style for solving complex programming problems.

- Top down approach - recursion + memoization, start from end of the problem
- Bottom up approach - dynamic programming table design, start from the beginning of the problem
- Recursion is when a function calls itself
- Memoization - remembering / caching function calculations and returning when same function get called again.
- Directed acyclic graph (DAG) - is a directed graph, that contains nodes connecting edges without cycles. Directed graph edges go only one way (defined direction). It is impossible to traverse the entire graph starting at one edge. Acyclic means that that are no loops (cycles) in the graph, meaning that there is no way to go back from on node (vertex) to another via the edge. An example of where DAG is used is a topological sort algorithm. This algorithm can be used anywhere where we have dependencies (if one thing depends on another e.g. determining order of tasks in a Makefile).

## Backtracking

- Enables to go through all possible search options meaning that ways of arranging objects or ways of building them. 

## Resources

- Lists - (University of Wisconsin–Madison) http://pages.cs.wisc.edu/~deppeler/cs367-common/readings/Lists/
- Abstract Data Types (GeeksforGeeks) - https://www.geeksforgeeks.org/abstract-data-types/
- The List Abstract Data Structure (Queen Mary University of London) - http://www.eecs.qmul.ac.uk/~mmh/ItP/resources/lists.html

## General resources

- Data structures - https://www.cpp.edu/~ftang/courses/CS240/notes.htm
- Complexity and Big-O Notation - http://pages.cs.wisc.edu/~vernon/cs367/notes/3.COMPLEXITY.html
