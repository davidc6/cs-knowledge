# System design

## Databases

* Relational - data stored in tables, rows. Relation DBs work best with structured data. Because of the constrains that are imposed on relationship in the system, there is a high level of data integrity. Join operations can be performed across tables. Data is organised by record and is kept next to each other in memory.
  * PostgreSQL
  * MySQL
* Non-relational - join operations are generally not supported in these category of databases. Great for dealing with large quantities of complex, diverse and unstructured data.
  * Key-value 
    * Redis
  * Graph
    * Neo4j
  * Column oriented (columnar) - data stored by column rather than by row. These databases are optimised for retrival of columns of data. This make them great for analytics and data warehousing when you need to query for a specific field.
    * Apache Cassandra
  * Document - 
    * MongoDB

* Both row and column databases can serve as a backbone in a system to serve data for ETL tools.
* ETL - extract, transform and load is a technique often used in data warehousing and involves copying data from a source (or many sources), transforming it into a shape that a destination system supports and saving it to the destination that represents the data differently from the source(s).

### Failover and redundancy

* To address these problems we use a technique called database replication. This can be implemented using a primary secondary relationship between the original database and copies. Primary database generally supports only write operations and secondary databases get copies of data that primary database holds. Primary database notifies secondary databases and each secondary database gets updated. Most frequently, systems are more read than write heavy and therefore the number of secondary databases and higher.

## Horizontal and vertical scaling

* Vertical scaling is adding more power (CPU, RAM) to a machine. The downside to this techniques is that there is hard limit to how much power can be added to a single machine. Additionally, if a single machine is used to serve application and it fails then users won't have access to it. Additionally, if there's a spike of traffic and many users trying to access the server then web server's limit might be reached. This will mean slower response times for users or failure to connect.
* Horizontal scaling is adding more servers instead of adding more power to each server. This technique is desired for large scale applications.

## Database scaling

You can have a really powerful machine with lots of RAM and CPU. But as with any hardware there are limits and it powerful machines are expensive. Additionally, a single machine will be a single point of failure.

A better approach is to horizontally scale by adding more servers and splitting a database into smaller, easily managed "shards". This technique is called database sharding. Each shard contains same schema but data is unique in each shard. One of the most important concepts when implementing sharding is the choice of the sharding key that determine how data is stored and distributed. Sharding key allows us to route queries to the correct database.

There issues associated with sharding such as resharding data (no more free space on a shard, uneven data distribution), join queries (denormalise data to perform queries in a single table since normalised data means more joins hence slower query), overwhelming certain shards because of the popularity of data on these shards.

## Cache

Cache layer is used to speed up system performance, avoid unnecessary / duplicate / identical database calls and improve user experience. Cache layer is a temporary data store that server data much faster due to (in many cases) being stored in RAM (in-memory cache). There various caching strategies. One of the more popular ones is read-through cache when a web server checks cache for data first and if it's available serves is from cache otherwise goes to the databases.

Use a cache system when the application is read-heavy and not write / update-heavy. Do not use a cache system for persistent storage since you will lose data when / if it restarts. Avoid single point of failure by deploying multiple cache servers. It is important to keep data in store and cache in sync for consistency. Keeping cache in sync across multiple regions is challenging. Setting expiration date is also necessary to avoid keeping old data in cache. Add cache eviction policy (e.g. LRU, FIFO, etc.) to specify what data to remove when cache is full.

## Static assets

In large scale applications, static assets (CSS, images, JS, video files) are usually cached by CDN (Content Delivery Network) servers that are located in various places in the world. A user will request for an asset and if a CDN has it (and it is valid meaning that it has not expired (valid TTL - time to live)), it will serve it otherwise it will fetch it from the origin (web server, S3, etc.), serve to user and store it in its cache.

Use a CDN when you want to cache frequently accessed assets, implement a fallback strategy in case CDN fails, use an appropriate cache expiry time (you will probably need to experiment with it depending on the asset), it also important to be able to invalidate cached asset (for example if you need to deploy a new JS bundle) which can be either done via CDNs API or versioning or hashing the assets.

## State

With horizontal scaling we need to take care of application state (user sessions, client data, etc.) This can be problematic because of the nature of single server applications. We need to start thinking about moving user session data out into a data store. This allows any server (when we scale the number of servers) in the cluster to access session data. 

A stateful server remembers client's state between requests whereas stateless server does not keep any state. This means that to "recognise" the user, the request should be routed to the server that contains that user's data. This architecture can be achieve by using the sticky sessions technique where load balancers assign some sort of an identifier to each client and then route traffic based on that identifier. This techniques comes with a number of cons and challenges and is not the "cleanest" approach.

A stateless approach is to add a shared data store (could use a non-relational or key-value store) where state data will be stored and each server can access it when necessary. This approach is cleaner, simpler and scalable. 

## Message queues

A message queue is a component that acts as a buffer is used for asynchronous communication in distributed systems. It must be durable and stored in memory. Messages get published to a message queue and are generated by publisher (input) services. Consumer services connect to the queue and perform actions defined by the messages from the queue (think pub / sub pattern here). This enables the queue to buffer a number of messages and enable subscribes to read those messages whenever they become available. Producers and consumers can be scaled independently.

## Monitoring, alerting and logging

Todo

## Data center location

Todo

### Things to always take into consideration

* Pick right type of database for the jobs
* Add cache systems when appropriate and use / cache as much as possible
* Use CDN to host / cache static assets
* Keep the system stateless by storing state in a data store
* Redundancy and every level in the system to enable high availability
* Have multiple data centers support the application
* Use database sharding
* Monitor the system and use automation
