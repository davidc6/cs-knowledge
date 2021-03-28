# Programming languages and concepts

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

Partial application - "partial applies a function", allows to pre-set one or more inputs and produce a function that expects the rest of the inputs.

Currying - a way of getting more and more specialised functions by passing one argument after another. Currying takes one input as a time. I can be thought of as a chained series of unary functions. Both currying and partial application are techniques used for function specialisation.

```js
const someFunc = a => b => c => a + b + c

someFunc(1)(2)(2) // manual currying
```

Continuation-passing style (CPS) - is a style of programming where continuation controls the flow as oppose to direct control. A CPS style function takes a function as an extra argument and once the result has been computed that function gets called and result passed as an argument.

```js
function getId(id) {
  return id
}

// cps
function getId(id, ret) {
  ret(id)
}
```

Lazy evaluation - 

Pattern matching - 

Thunk - 

Tail call (tail call optimisation) - 

### Resources

- By example: Continuation-passing style in JavaScript - http://matt.might.net/articles/by-example-continuation-passing-style/
