# Search autocomplete

Sometimes also refered to as "design top K" / "design top K search queries".

## 1. Establish scope, clarify

Q: Is the matching supported at the beginning of a search query or middle as well?
A: Beginning

Q: How does the system know which top results to return?
A: Popularity, decided by frequency of historical queries

Q: How many queries suggestions to return?
A: 5

Q: Query language?
A: English

Q: Cap or special chars?
A: All queries lowercase

Q: How many users use the product?
A: 10 million DAU

- Fast response (within 100ms)
- Relevant
- Sorted by popularity
- Scalable (can handle high traffic)
- Highly available

### Back of the envelope estimation

- 10 million users DAU
- 10 searches a day
- 20 bytes of data per query
  - ASCII, 1 char is 1 byte
  - Query is 4 words, 5 chars on avg, 4 * 5 = 20 bytes per query
- For each char we make a request to backend, 20 requests per query max
- 10,000,000 users * 10 searches per day = 100,000,000 searchers per day
- 100,000,000 * 20 bytes = 2,000,000,000 bytes per day
- QPS = roughly 24,000
- Peak QPS = QPS * 2 roughly 48,000
- 20% of daily queries are new roughly 0.4GB of new data stored daily

## 2. High level design

There two components:

1. Data collection

We store each keyword in a frequency table and number of times it has been searched for:

```
Keyword: hello
Freq: 1
```

## 2. Data query

As a user starts typing we can select all records that match users search requests.

```sql
SELECT * FROM frequency_table WHERE query LIKE `prefix%` ORDER BY frequency DESC LIMIT 5
```

As the data set grows this will become less performant. We need a different solution.

## 3. Deep dive

The main components are:

- Trie data structure
- Data gathering service
- Query service
- Storage scale
- Trie operations

Trie is a tree data structure which allows us to store a character in each node and 26 children 
representing 26 characters for each possile character. Each node stores a single character or a string 
which represents either the whole word or prefix. Each node that has a complete word will contain character 
frequency count in it.

In order to find suggestions, we need to find prefix (O(n) n is length of prefix), get all child nodes (O(x) x is number of 
children, sort by popularity O(c log c). So O(n) + O(x) + O(c log c).

To speed this up we could limit the number length of prefix or cache top results at each node.

By limiting the length of prefix we achieve O(1) and by caching results at each node we achieve O(1).
However we do increase memory usage as we store data at each node. However for fast response time this is 
a good trade-off.

### Data gathering service

Previously search data is updated in real-time which is not practical as usesrs may enter billions of queries per day. Updating 
trie on every query slows down the service, top suggestions maybe not change often. We store queries in append only fashion for 
analytics purposes. Data then gets aggregated. We might do this once a week. Time of aggregation might be the start of the week 
and frequency how many times the same data was queried for. 

Then workers will pick this data up from the database and build a trie in a trie db. We could also potentially cache it by using 
a trie distibuted cache. We could use mongodb for storing a string all its' children.

Since query service needs to be fast, we can make AJAX (async requests) to store the data. Additionally, since searcgh result won't 
change much we can store them in browser cache for 1 hour or so.

We can also ut a filter in front of the trie cache to remove any unwanted content. This can be based on user filter settings.

To scale the storage (and since we are using only one language), we can shard databases on 'a - m' and 'n - z' letters. We can 
even go further and split into 26 servers for each letter of the alphabet. This might not be the best solution as 
some letter have more words start with those letters and we need a different strategy. We can analyze historical data distribution 
and create shards based on that. So we could have a shard for 'a' and 'b to d' which will be distributed equally.




