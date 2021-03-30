# System design

## Databases

* Relational - data stored in tables, rows. Relation DBs work best with structured data. Because of the constrains that are imposed on relationship in the system, there is a high level of data integrity. Join operations can be performed across tables.
  * 
* Non-relational - join operations are generally not supported in these category of databases.
  * Key-value - 
    * Redis
  * Graph - 
    * Neo4j
  * Row - data is organised by record and is kept next to each other in memory. Great for dealing with large quantities of complex, diverse and unstructured data.
    * PostgreSQL
    * MySQL
  * Column oriented (columnar) - data stored by column rather than by row
  * Document - 

* Both row and column databases can serve as a backbone in a system to serve data for ETL tools.
* ETL - extract, transform and load is a technique often used in data warehousing and involves copying data from a source (or many sources), transforming it into a shape that a destination system supports and saving it to the destination that represents the data differently from the source(s).

### Failover and redundancy

* To address these problems we use a technique called database replication. This can be implemented using a primary secondary relationship between the original database and copies. Primary database generally supports only write operations and secondary databases get copies of data that primary database holds. Primary database notifies secondary databases and each secondary database gets updated. Most frequently, systems are more read than write heavy and therefore the number of secondary databases and higher.

 
## Horizontal and vertical scaling

* Vertical scaling is adding more power (CPU, RAM) to a machine. The downside to this techniques is that there is hard limit to how much power can be added to a single machine. Additionally, if a single machine is used to serve application and it fails then users won't have access to it. Additionally, if there's a spike of traffic and many users trying to access the server then web server's limit might be reached. This will mean slower response times for users or failure to connect.
* Horizontal scaling is adding more servers instead of adding more power to each server. This technique is desired for large scale applications.

## Static assets
