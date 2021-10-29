# Functional programming

## Concepts

- Control flow - handled by expressions and functions
- Handling state - state exists only inside (pure) functions and result returned and passed to other functions
- Branching logic - no `if`'s, conditional expression instead
- Loops / iterations - recursion
- Cache - a technique called memoization is used to store computations
- Identifiers - in pure functional programming, assignments are not encourages (if at all allowed) and are handled inside functions and call arguments
- Inheritance - 

## Pure function

A function that takes same input and returns same output every time is a pure function. 

Some benefits of using pure functions:

- Testing - pure functions are easily testable, same input same output.
- Modular - pure functions can essentially be moved around the codebase / copied, etc. since the logic is contained within the function.
- Caching - pure functions can be easily cached by using a technique called memoization. For instance if the function gets called twice with the same argument, instead of running the logic again we can return the cached result.
- Parallelism - since pure functions do not need access to the shared memory they are great when writing parallel code.
- Reasonable code - when any expression in our code can be replace with its' value without effecting the program it is referentially transparent. Since we can replace expressions with their values we can reason about our code which is great for understanding and debugging our code.

## Partial application

"Partial applies a function", allows to pre-set one or more inputs and produce a function that expects the rest of the inputs.

## Currying

Currying is a way of getting more and more specialised functions by passing one argument after another. Currying takes one input as a time. I can be thought of as a chained series of unary functions. Both currying and partial application are techniques used for function specialisation.

```js
const someFunc = a => b => c => a + b + c

someFunc(1)(2)(2) // manual currying
```

## Continuation-passing style (CPS)

CPS is a style of programming where continuation controls the flow as oppose to direct control. A CPS style function takes a function as an extra argument and once the result has been computed that function gets called and result passed as an argument.

```js
function getId(id) {
  return id
}

// cps
function getId(id, ret) {
  ret(id)
}
```

## Functors

A mathematical definition of a functor is a mapping between categories. Functional programming takes inspiration from math and defines functors as an object that can map (apply) a function to its' data without changing the structure of it.

### Identity functor

- Identity functor enables us to map over a value
- If map is given to an identity function it must return the exact same object

## Morphism

- When one structure gets mapped to another but preserves the type
- You can think of morphisms as functions
- Morphisms can be composed
- Identity morphism is when an arrow goes from one object to itself
- Polymorphic functions work with any type it's given

## Polymorphic

- A polymorphic function is a function that can return multiple types

## Lazy evaluation

Todo

## Pattern matching

Todo


## Thunk

Todo

## Identity function

- A function that takes an argument and returns an argument

## Types (datatypes)

- Types are a way of categorising / grouping values together such as `string`, `character`, `number`, etc.
- Every value has a type
- 
- Types are important for safety, readability and maintainability of programs
- A `type constructor` is the name of the type
```ts
// TypeScript
type Car {}
```
- Type signatures are type level of code
```ts
// TypeScript
function appendStrings(a, b): string {}
```
- Data constructors (values that are used, defined, evaluated in code) populate the types they are defined in

### Product types

- Types that are expressed / built using `AND` operator
- Similar to a struct in C
- The ability to contain / carry multiple values in a single data constructor

### Sum types

- Types that are expressed / built using `OR` operator

### Error handling

- https://adambard.com/blog/acceptable-error-handling-in-clojure/

## Haskell

- Does not have any notion of objects. When a value is constructed (instance of
  a type), the constructor creates a box about the value which then gets passed
  to functions.

### References

- https://wiki.haskell.org/The_Monad.Reader/Issue3/Functional_Programming_vs_Object_Oriented_Programming

## Resources

- By example: Continuation-passing style in JavaScript - http://matt.might.net/articles/by-example-continuation-passing-style/
- LofTech with Philip Wadler - Why some people use Functional Languages? - https://www.youtube.com/watch?v=bjcLYLPJg8w
- A Guide to Functional Programming Lingo for JavaScripters - https://gist.github.com/ericelliott/ea925c58410f0ae74aef
