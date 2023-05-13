# General

## Virtual machine

- VM is an emulation of a computer system which provides all of the functionality of one.

## Hypervisor

- It is a computer software that is used to create and run virtual machines and provides a platform for machines to run on. The machine the hypervisor is running on is the host machine and the vm is the guest machine.

```
// simplified diagram
hardware -> OS (host machine) -> hypervisor -> VM (guest machine) -> OS -> Application
```

## CPU architectures

### Popular processor architectures

- 32-bit - e.g. `x86`, `ARM`
- 64 bit - e.g. `x86-64`, `ARM64`

## Kernel

- Is the core and central part of an operating system that controls everything and acts as the link between the hardware (CPU, memory, etc.) and software components.

## Blob (BLOB)

- Blob is essentially binary data stored as a single entity. This could be an audio / video file, image etc.

## General useful terms

- **Idempotence** - the term generally means that an operation can be applied multiple times without causing unintended effects. As an example, an update to user details is usually idempotent since we can apply the same operation multiple times but the result will be the same. An opposite to that is if a user makes an order, they can make it a number of times and multiple orders will be placed.
- **function expression** - when a function (named or unnamed) is created inside of an expression it is called a function expression; an expression is a combination of values and functions combined to create a new value.

```js
// assignment operator here is a type of expression
const thisIsAFunctionExpression = () => {
  console.log('Hello!')
}
```

- **function declaration** - defines a function that is given name and contains parameters; it is essentially a standalone function / unit of execution

```js
// function declaration, a standalone unit of execution
function thisIsAFunctionExpression() {
  console.log('Hello!')
}
```

- POSIX - a set of standards that defines API (application programming interfaces), shells and utilities that allows to maintain compatibility between software and operating systems.

## Web

### WebRTC (protocol)
 
- Real time web communication. WebRTC is peer-to-peer. It allows us to send and receive an unlimited amount of audio and video streams.

### WebM

- It is a file format. It is a container that containers video and audio. This is an example of a static file that sits on the server and gets passed / delivered to clients. This technique is called progressive download.

### X11

https://unix.stackexchange.com/questions/12755/how-to-forward-x-over-ssh-to-run-graphics-applications-remotely

### Misc

- Byte stream - contains bytes, what these bytes are completely depends on the context.
- Advanced Message Queueing Protocol  https://www.amqp.org/ - 
- JavaScript Expressions and Operators - https://hepunx.rl.ac.uk/~adye/js10/expr.html
- 
