# Observability

- Logging - output logs, log streaming service, what should logs show?
- Trace request through multiple services (headers on request)

## Logging

- Log what is coming into the system and what is going out
  - Request from a user, route, user agent, time, form data etc.
  - Response: status code, stack
  - For databases, this could be logging a query and response from the db
  - Batch jobs, when started / finished, failures, timestamps
  - Make sure to always include timestamps

Emitted by each process and contain information about about it, debugging information,

Monitoring levels:
	- OS - sends logs already
	- K8s - sends logs already
	- Applications - (event stream) instrument good logging system

-> goes into log aggregator (which has filters)

## Monitoring

- Monitor health of our application
- Send information (automated alerts) about certain events in the system

## Metrics

Monitoring - what is actually running in the application.

Percentile - for instance 95% percentile, 5% will exceed a threshold. Let's look at the graph at 
https://api.contentstack.io/v2/assets/575e4c719985d58976376589/download?uid=blte0e63d25a4006d9c?uid=blte0e63d25a4006d9ci 
we can see that at 9:30am the mean (average) latency is 75ms, however 99th 
percentile says that 99% of values is less than 850ms and 1% is more than 800ms, 
which could be a bad sign for the business.
Mean - 
Median - 

## Resources

- Logging best practices: the 13 you should know - https://www.scalyr.com/blog/the-10-commandments-of-logging/

