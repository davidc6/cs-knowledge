# What is a Socket?

A socket a method of communication that allows processes to pass data to each other either on the same or different hosts (computers) via various protocols (such as TCP). A socket is a virtual device. Socket connection is full duplex and allows for two way communication.

## Unix domain socket

This type of socket allows for efficient communication between processes locally (meaning the same host). This is also know as local interprocess (or inter-process / inter process / IPC) communication.

## Network socket

This type of socket allows communication between processes that are located on different hosts. Each network socket has a socket address. The format of this address is Internet address plus a port.

```
internet-address:port
```

A client is requesting for data and a server is providing such information. A client's socket port is assigned by the kernel when a connection request is made. This port is a ephemeral number (meaning that it is short-lived) used by the IP protocol. Server socket consists of an Internet address and a well know port associate with the service (for example web servers run on port 80). A connection is identified by the two endpoints called socket pair and is a tuple:

```
// cliaddr is the client Internet address and serveraddr is the server Internet address
// cliport is the client port and servport is the server port
(cliaddr:cliport, serveraddr:servport)
(128.2.194.242:21564, 208.126.134.34:80)
```
The socket interface which was developed by the researchers at University of California, Berkleys in the 80s, is a set of functions that used together with UNIX I/O functions to build network applications. Socket interface has been implemented on most modern systems.

## Socket programming

Socket programming is a way of connecting two nodes on a network to communicate with each other.

## Socket limits

* 64K per client per server limit. Real limit is file descriptors. (Reference?)

## Resources

* (book) The Linux Programming Interface: A Linux and UNIX System Programming Handbook
* (book) Unix Network Programming, Volume 1: The Sockets Networking API
* (book / html) Beej's Guide to Network Programming - http://beej.us/guide/bgnet/
* (book) Computer Networking: A Top-Down Approach
