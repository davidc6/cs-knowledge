# Messaging

## Polling

Todo

### Long polling (aka COMET)

### Short polling

## WebSocket

Todo

## Server sent events (SSE / Event streaming)

This method of messaging is useful when bidirectional communication is not needed. For example:

* Real time updates of product availability
* Stock prices (or any data that is frequently changing)
* Feeds (news, activity, etc.)

### Key points

* Server to client, one way communication (unidirectional)
* Enables data stream events via HTTP
* Server pushes data without client having to request for it
* Very similar to WebSockets but one-way
* Part of browser HTML5 spec
* [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) interface is used to work with SSE which opens a persistent connection to a server 
* [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) also supports this feature
* Browser support can be an issue (https://caniuse.com/?search=eventsource)

## Resources

* WebSockets for fun and profit - https://stackoverflow.blog/2019/12/18/websockets-for-fun-and-profit/
* Server sent events - https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
