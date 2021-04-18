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

### Tail call

Todo

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
