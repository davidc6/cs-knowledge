# Database

There are many different purposes that a database management system can serve. This could be for storing long-lived storage, complex analytics queries, storing time-series data, temporary data or large blobs of data.

There isn't a single blueprint for database management system design. Below are some common components that databases consist of.

## Architecture

- [Transport](#transport)
- [Query Processor](#query-processor)
- [Execution Engine](#execution-engine)
- [Storage Engine](#storage-engine)

### Transport

The transport layer is essentially responsible for handling communication between the client and DBMS. It can handle things like: 

- Connection establishment
- Authentication
- Protocol management
- Session management

This is sometimes also referred to as "client communications manager". Once again its' mission is:

- to establish and remember the connection state for the caller
- to respond to commands from the caller
- to return data and control messages (error codes, errors, etc.)

This component can be broken down into these sub components: 

- Cluster Communication - this component is responsible for communicating with other database nodes in a cluster, also load balancing.
- Client Communication - client requests travel through this component. These requests are essentially queries in some form of a language. 

The transport then pushes the command deeper into the database.

### Query Processor

- From the **transport layer**, the query is handed over to a query processor that parses and processes (interprets and validates) it.
- Access control checks are done only after the query is fully parsed.
- Once parsed the query is parsed to **query optimizer**. 
- Query optimizer
    - Removes impossible parts of the query
    - Attempts to most optimal way to execute the query based on
        - Index cardinality
        - Approximate intersection size
        - Data placement (nodes in the cluster that hold the data and cost of transfer)

### Execution Engine

- A database query is presented as an execution plan, that is a sequence of operations
- Optimizer picks the best plan
- This plan is handled by the **execution engine**
- **Remote execution** is about writing and reading data to and from nodes in the cluster

### Storage Engine

It is an underlying component that a database uses to store, retrieve and manage data and on disk. It is designed to capture persistent, long-term memory of each node. DBMS systems are built on top of storage engines 

#### Transaction Manager



#### Lock Manager

- Manages locks on objects for the running transactions
- Ensures that concurrent operations do not violate data integrity

#### Access Methods (Storage Structures)

#### Buffer Managers

#### Recovery Manager


## Commit logs (write-ahead logs / WALs)

WALs a sequence of records each with its own unique identifier. You can append to the end of the logs but you cannot mutate them (they are immutable). Commit logs are called write ahead logs (WALs) in PostgreSQL. First, data is added to the write ahead log and before it is changed in either a table or index. Every B-Tree modification must be written before it can be applied. For example, if a database crashes, the log is used to restore the B-Tree (db index/indexing implementation structure) to a consistent state.

B-trees break the database down into fixed-sized blocks or pages (4Kb in size). These read and write one page at a time. This design corresponds really well with the hardware design such that disks are also arranged in fixed-size blocks. 

SSTables - similar to B-trees are sorted by keys (allows for efficient key-value lookups and range queries). 