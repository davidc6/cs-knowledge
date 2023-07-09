# C

## Storage duration

Objects have 4 storage durations:

- Automatic
- Static
  - Objects that are declared in a file scope have this duration and have a
    lifetime the entire execution of the program
- Thread
  - Used in concurrent programming
- Allocated
  - Dynamically allocated memory

## Structure

Structs can have a structure tag, structure definition at end (before the
semicolon) 

```
struct [structure tag] {
  member defintion;
  ...
} [structure variables]
```

## Type definitions

`typedef` is used to declare an alias for an existing type, it doesn't create a
new type. 

## Types

`char` - there isn't a character type in C, it is the smallest integer type. 
`signed char` - negative, zero and positive values

## Memory management

- `malloc()` - 
- `calloc()` - 
- `realloc()` - 
