# Database

## Storage engine

It is an underlying component that a database uses to store, retrieve and manage data and on disk. It is designed to capture persistent, long-term memory of each node. DBMS systems are built on top of storage engines 

## Commit logs (write-ahead logs / WALs)

WALs a sequence of records each with its own unique identifier. You can append to the end of the logs but you cannot mutate them (they are immutable). Commit logs are called write ahead logs (WALs) in PostgreSQL. First, data is added to the write ahead log and before it is changed in either a table or index. Every B-Tree modification must be written before it can be applied. For example, if a database crashes, the log is used to restore the B-Tree (db index/indexing implementation structure) to a consistent state.

B-trees break the database down into fixed-sized blocks or pages (4Kb in size). These read and write one page at a time. This design corresponds really well with the hardware design such that disks are also arranged in fixed-size blocks. 

SSTables - similar to B-trees are sorted by keys (allows for efficient key-value lookups and range queries). 
