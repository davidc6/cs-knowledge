## Crawler

Crawlers also know as web crawlers, spiders, bots, robots are systems that regularly and automatically crawl the Web. A crawler usually has a set of pages that it starts with and then follows links on those pages to collect more information. It is a recursive action.

Search engines use crawlers to collect and index web pages, some job boards use crawlers to aggregate jobs postings, crawlers are also used for data mining.

### Flow

- Download web pages by the given URLs (seed URLs)
- Extract URLs from these pages
- Add URLs extracted from these pages to the list of urls that need to be downloaded

Crawlers are usually very complex systems and contain many components.

- The web has many things a crawler has to be ready to deal with. These are such things as: broken or malicious links, unresponsive serves, etc. So the crawler has to be robust.
- Since there are billions of pages on the web, the crawler has to be scalable.
- The system has to be maintainable and extensible. For instance if we want to support a new component or an old one, we should be able to "plug'n'play".
- Crawlers also have to be polite, meaning that they should be sending lots of traffic to web pages within a short time frame.

### Estimations

- 

### Components

- Seed URLs - a list of URLs that will serve as a starting point for our crawling process
- URL Frontier - this component is used for storing URLs to be downloaded
- Downloader - used to download pages from the URLs provided by the URL Frontier
- DNS Resolver - enables the crawler to get IP addresses of web pages
- Parser - downloaded content should be parsed and verified to prevent any broken pages from being stored
- Duplicate checker - checks hashes of downloaded pages to avoid storing duplicate information
- Storage - downloaded pages are stored on disk
- URL extractor - enables to extract urls from downloaded pages
- URL filter - filters URLs (extension, disallow list, content type)
- URL list - is a data structure that keeps track of visited URLs and URLs that are currently in the URL Frontier
- URL storage - stores visited URLs
- 

### Approaches

- The process of crawling can be thought of as graph traversal
- Each web page is a node
- Each link is an edge
- Traversal takes place from one web page to another
- The choice of how to traverse is between BFS and DFS
  - DFS - depth-first search, depth first and this can be very deep
  - BFS - breadth-first search, breadth first and usually is a better option
    - When processing internal pages, BFS might flood the web page with requests so some sort of a crawl prioritisation / importance technique is required to make sure that the crawler is polite
- URL frontier data structure helps with page prioritisation. If the crawler is not polite the traffic from it might cause an unintentional DDOS attack. Downloading on page at a time, having delays between request make crawlers more polite.
    
#### URL Frontier

- 

#### Downloader

This component downloads pages from the Web using HTTP protocol. It is important to refer to `robot.txt` file in order to understand what the crawler is allowed to download. This file is normally downloaded and cached by the crawler.

Crawl jobs are distributed amongst several servers and which run multiple threads. Each downloader is responsible for a set of URLs that come from a URL space.
