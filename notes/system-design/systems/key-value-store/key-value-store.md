# Key Value Store

## Single server

- We can store all data in a single hash table
- Storing data on single server is limiting
- We can compress the data
- We can keep only most frequently accessed data in memory (could cache rest on disk)
- Best is to make this a distributed hash table

## Distributed

- System can be distributed amongst many servers/instances
- We can only choose two out of 3 CAP properties (Consistency, Availability, Partition Tolerance)

## System components

- Data partition - data needs to be split into smaller partitions and stored on multiple servers
- Data replication - data has be replicated in the event of primary node failure (to achieve high reliability)
- Consistency - data has to be made readily available regardless of the server that the client is connected to
    - Consistency models
        - Strong consistency - any read operation returns a value corresponding to the result of the most updated write item, in order words client never sees out-of-date data. 
            - Replicas are usually forced not to accept new reads/write while every replica has agreed on current write. 
            - For highly available systems this is not ideal.
        - Weak consistency - subsequent read operations may not get the most updated value
        - Eventual consistency - a form of weak consistency. Given enough time all updates are propagated and replicas are consistent
            - Dynamo and Casandra adopt this model (eventual consistency)
- Inconsistency resolution - replication high availability causes inconsistencies amongst replicas
- Handling failures - 
- System architecture diagram - 
- Write path - 
- Read path - 

## Data Partition

- It is not feasible to store all the data on a single server
- Data has to be split into partitions and stored on multiple servers
- Data partitioning has challenges
    - Even data distribution across multiple servers
    - Remove or addition of a new server should not cause too much data  movement
- **Consistent hashing** (a technique that assigns data and nodes a position on
a virtual ring structure i.e. hash ring) can be used to solve the above
    - IP/domain name of a node % by total number of available positions on a hash ring
    - The result is the position of the node on the hash ring
    - Data is hashed using the same technique and then the ring is traversed (clockwise) until
    a node is found where the data is then stored
- 