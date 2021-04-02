## Design activity feed

This is a component that allows a user to see activities of their friends. Let's say you want to see what audio you friends recently played.

Components:

* Activities
  * service - for saving and retrieving activities
  * database - for persisting activities data
  * cache - for fast retrieval of activities
* Users
  * service - for saving and retrieving users
  * database - for persisting users data
  * cache - for fast retrieval of users data
* Fan-out service - enables to push updates to user's friends activity feeds when new activity is detected
* Notification service - to notify users about updates
* Friends / Connections Graph DB - persists connections / friends data

### Activity publishing  (write activity)

* Activities publishing API

```
// post request to endpoint
POST /v1/activities

// with the following parameters
audio_id="music-track-1"&action="played"&auth_token="some-auth-token"
```

#### Design

* A user starts playing an audio track
* A POST request is made to an endpoint /v1/activities
* Activities service persists activity to database and cache
* A (fan-out) service gets user's connection ids from a Graph database
* A (fan-out) service pushes new activity and connection ids to the message queue
* Workers pop data from the message queue when available and store in activities feed cache for fast retrieval. The limit can b configured and cache missed are expected on previous activities.

```
activity_id: 1,
user_id: 2
```

* (Optional) Notification service - informs users that new activity is available 

### Activity building / retrieval - aggregation of posts in chronological order (read activity)

* Activities retrieval API

```
GET /v1/activities

auth_token="some-auth-token"
```

#### Background

* Post will be populated on friends news feed
* The activities feed is built by aggregating friends' activities in a reverse chronological order

#### Design

* A user makes a request to `/v1/activities` endpoint

* Activities service fetches user's activities ids from cache (user_id, activity_id)
* Then the service retrieves information about user
* Then the service retrieves information about activity
* Activities get hydrated
* Activities feed is returned in JSON

### Cache

TODO
