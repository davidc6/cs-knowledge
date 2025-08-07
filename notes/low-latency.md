# Low Latency System

## Thread pool

A thread pool is used to reuse existing threads rather than destroying and recreating 
them for each new task. With this approach we can optimise resource allocation, 
task execution in parallel, concurrency control, thread load balancing, mitigate
context switching and more.

There can be different types of thread pools. There are thread pools for CPU-bound work,
for network-bound tasks.

### CPU-bound tasks thread pool

If an application is bottlenecked on CPU, we want to maximise CPU resources. For 
a CPU of 8 cores, it would be good recommended to have a minimum of 8 threads running 
at any given time. If more than 8 threads are utilised then the CPU would have to 
context switch. This can slow things down as memory locations matter for performance. 

Memory access is slow. The performance cost associated with context switching is 
in the lost state of the process in the CPU caches, instruction pipeline, 
branch prediction and TLB cache. 

### Network-bound tasks thread pool

When an application deals with a lot of network-bound tasks (such as querying a db, 
sending metrics etc) then a CPU cores are really irrelevant since most of the times
the time is spent on waiting for a response and not processing.

Multiple concurrent operations have to be handled hence the need for an async library. 
Threads are not needed if using async libraries. 

Threads can be used for example if async libraries are not an option, for example. 
The number of threads will depend on the number of concurrent operations that need
to be done (10 requests = 10 threads etc.). 

In this context a thread pool is a useful tool to use since at some point, an 
application might start hitting resource (OS limits on file descriptors, db connections etc)
and concurrency limits. Thread pool will enable us to put an upper bound limit.
