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


