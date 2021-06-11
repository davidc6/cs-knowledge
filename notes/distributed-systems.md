# Distributed systems

## CAP theorem

CAP theorem states that in a distributed system it is impossible to guarantee more than two of the three characteristics:

- Consistency - all clients should see the same data at all times, the node that they are connected to should not make a difference in what data the clients are seeing. A write is a successful one if all nodes in the distributed system have the same data (forwarded / replicated)
- Availability - any request for data from a client will always result in a response even if some nodes are down
- Partition tolerance - a cluster should continue to operate even if there's a loss / delay of connection between nodes in a system

## IPC (inter-process communication)

- The ability of an operating system to enable processes to manage shared state. `Independent processes` cannot be effected or effect other processes in the system. `Cooperating processes` can effect or be effected by other processes in the system. If two processes are sharing data then they are `cooperating processes`.
- The reason to use inter-process communication is done for: information sharing, increase computational speed

## RPC (remote procedure call)

- A remote procedure call is when a computer program calls a procedure is called on another computer. This is normally done on a shared network but the procedure is coded just like a normal local procedure without specifying details of remote interaction.
- 

## Resources

- CAP Theorem - https://www.ibm.com/cloud/learn/cap-theorem
- Interprocess Communication in Distributed Systems - https://www.geeksforgeeks.org/interprocess-communication-in-distributed-systems/
- Interprocess Communication - https://www.youtube.com/watch?v=dJuYKfR8vec
