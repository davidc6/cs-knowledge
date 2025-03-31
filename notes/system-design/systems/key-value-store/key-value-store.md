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

- **Data partition** - data needs to be split into smaller partitions and stored on multiple servers
- **Data replication** - data has be replicated in the event of primary node failure (to achieve high reliability)
- **Consistency** - data has to be made readily available regardless of the server that the client is connected to
    - Consistency models
        - Strong consistency - any read operation returns a value corresponding to the result of the most updated write item, in order words client never sees out-of-date data. 
            - Replicas are usually forced not to accept new reads/write while every replica has agreed on current write. 
            - For highly available systems this is not ideal.
        - Weak consistency - subsequent read operations may not get the most updated value
        - Eventual consistency - a form of weak consistency. Given enough time all updates are propagated and replicas are consistent
            - Dynamo and Casandra adopt this model (eventual consistency)
- **Inconsistency resolution** - replication high availability causes inconsistencies amongst replicas
    - Vector clock is a common technique to resolve data conflicts and reconciliation issues
    - A vector clock [server, version] is associated with a data item
- **Handling failures**
    - Typically a couple of sources are necessary to confirm that a server is down in a distributed system
    - All-to-all multicast solution is not ideal when there are many nodes in the system
    - Gossip protocol (where several entities keep track of other nodes health/heartbeat) is a better decentralized failure detection solution
    - Temporary failures are handled by another server processes while the server that is down is ignored (once the server is back, data will be pushed to it) - this is called hinted handoff
    - A Merkle tree enables us to keep replicas in sync in a replica becomes permanently unavailable. It is used for inconsistency detection and data transfer minimization. Each piece of data is compared on replicas and updated to the newest version. 
    - Data center outages should be mitigated by replicating data across different regions
- **System architecture** - 
    - A node that a client connects to is a coordinating node
    - The above node acts as a proxy between the client and key-value store
    - Consistent hashing is used to distribute the nodes
    - Adding and removing nodes can be automatic since the system is decentralised
    - Data is replicated at multiple nodes
    - Every node has the same set of responsibilities so there isn't a simple point of failure. Each node: 
        - Client API 
        - Failure Detection and Repair mechanism
        - Replication
        - (Data) Conflict Resolution
        - Storage engine
- **Write path** - 
    - Request comes in and the write is persisted on a commit log file (on a disk)
    - Data get stored in the memory cache
    - When the memory hash is full it gets flushed to SSTable of the disk
- **Read path**
    - Node that the read request is directed to, checks if data is in the memory cache
    - If data is not in the memory it will be retrieved from the disk
    - A bloom filter can be used to find out which SSTable contains the key

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

## Summary

- Big data storage - consistent hashing to spread the load across servers
- High availability reads - data replication and multi-data centre setup
- High availability writes - data versioning and conflict resolution with vector clocks
- Dataset partition, incremental scalability, heterogeneity - consistent hashing
- Tunable consistency - quorum consensus
- Handling temporary failures - sloppy quorum and hinted handoff
- Handling permanent failures - merkle tree
- handling data center outage - cross-data centre replication
