# Programming languages and concepts

## General concepts

### Closure

Closure (lexical / function closure) - is a function that is aware and remembers / caches surrounding it variables. If you need to use variables over time, it is best to encapsulate them and allow inner functions to access them. When a function remembers scoped variables it does so via a closure.

```js
const increment = (a) => {
  let total = 0

  return () => {
    total = total + a
    return total
  }
}

const incr = increment(1)

incr() // 1
incr() // 2
incr() // 3
```

## Functional programming concepts

### Pure function

A function that takes same input and returns same output every time is a pure function. 

Some benefits of using pure functions:

- Testing - pure functions are easily testable, same input same output.
- Modular - pure functions can essentially be moved around the codebase / copied, etc. since the logic is contained within the function.
- Caching - pure functions can be easily cached by using a technique called memoization. For instance if the function gets called twice with the same argument, instead of running the logic again we can return the cached result.
- Parallelism - since pure functions do not need access to the shared memory they are great when writing parallel code.
- Reasonable code - when any expression in our code can be replace with its' value without effecting the program it is referentially transparent. Since we can replace expressions with their values we can reason about our code which is great for understanding and debugging our code.

### Partial application

"Partial applies a function", allows to pre-set one or more inputs and produce a function that expects the rest of the inputs.

### Currying

Currying is a way of getting more and more specialised functions by passing one argument after another. Currying takes one input as a time. I can be thought of as a chained series of unary functions. Both currying and partial application are techniques used for function specialisation.

```js
const someFunc = a => b => c => a + b + c

someFunc(1)(2)(2) // manual currying
```

### Continuation-passing style (CPS)

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

### Functors

A mathematical definition of a functor is a mapping between categories. Functional programming takes inspiration from math and defines functors as an object that can map (apply) a function to its' data without changing the structure of it.

### Lazy evaluation

Todo

### Pattern matching

Todo

### Thunk

Todo

### Tail call

Todo

### Types (datatypes)

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

#### Product types

- Types that are expressed / built using `AND` operator
- Similar to a struct in C
- The ability to contain / carry multiple values in a single data constructor

#### Sum types

- Types that are expressed / built using `OR` operator

### Resources

- By example: Continuation-passing style in JavaScript - http://matt.might.net/articles/by-example-continuation-passing-style/

## Concurrent computation

- Actor model - is a conceptual model that enables us to deal with concurrent computation by passing messages to actors (primitive unit of computation). Actor can act on such messages by running certain computations.
  - Most commonly this model is associated with Erlang programming language
  - In Erlang (and Elixir) an actor is a very lightweight process
  - Actors are isolated and don't share memory
  - Actors keep mutable state private
- Threads and locks - the idea behind this concept is simple, only one thread can access data at a time. This is achieved by using locks. This property of concurrency control is called mutual exclusion (mutex).
  - Race condition - 
  - Deadlock - is a situation where a thread tries to hold more than one lock
  - Thread - a single thread (unit) of control, communication between threads is done via the shared memory
  - Shared memory - 
  - 

## Language classifications

- Static - a language uses a static policy that enables the compiler to make decisions at compile time (C, C++)
- Dynamic - a language uses a policy that enables decisions to be made only at run time (JavaScript, Ruby)
- Statically typed language - performs type checking at compile time
- Dynamically typed language - performs type checking at run time
- Duck typing - type / class is less important (types are not checked) than a method or attribute presence (Python)
- Weak typed - a language that allows conversion between unrelated types, values are not "tied up" to a specific data type (PHP, JavaScript)
- Strongly typed - a language that does not allow conversion between unrelated types. A compiler in a strongly typed language guarantees that code will run without any type related errors. Values are "tied up" to a specific data type (Haskell, Scala)
- Type checking - a process of checking that code conforms to type system rules of a source language and is used to catch inconsistencies. It has the potential of catching errors in programs where operations are applied to the wrong type or wrong parameter is passed into a procedure.
- Expression - a combination of values and functions that are used to create a another value
