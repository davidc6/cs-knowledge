# Security

## General

- `CSP (content security policy)` - added layer of security to mitigate such attacks as XSS and data injection. Server should return `Content-Security-Policy` header
- `DNS prefetch control` - 
- `Expect CT` - 
- `Frameguard` - 
- Hide `powered by` - 
- `HSTS` -  
- `Data at rest encryption` - data is encrypted when on disk. This prevents attacker from accessing the unencrypted data. Without encryption keys.
- `Replay attack` - 

## Authentication

### Authentication vs authorization

- `Authentication` - who are you / your identity
- `Authorization` - what can you do / your role (permissions)

### HTTP basic authentication

`Basic authentication` is when a user agent provides username and password (base64 encoded) in the header. Below is a request example. `Authorization` header contains hello:world (username:password) base64 encoded.

```
GET https://www.somewebsite.com/test
Authorization: BASIC aGVsbG86d29ybGQ=
Host: https://www.youvegotleads.com
```

- No cookies, ids or any tokens are used in this method (easy implementin)
- Internal networks is a possible use case
- Not secure if used over HTTP (no TLS)

### HTTP digest authentication

Similar to basic authentication but aims to tackle weakness of basic authentication. One of such things is instead of using base64 encoding, it applies hashing (hash function) to username and password.

```
Authorization: Digest username="UserOne",
  realm="someuse@example.com",
  nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
  uri="/test/dir/index.html",
  response="6629fae49393a05397450978507c4ef1",
  opaque="5ccc069c403ebaf9f0171e9517f40e41"
```

- This method could be slow - since authentication details are checked on each request (password hashing functions are CPU intensive)
- Not a silver bullet

### Session-based / cookie-based authentication

Session-based (sometimes referred to as coookie-based) authentication is a way of maintaining user state in an application. When a user successfully logs in (`POST` request), a server generates a session, stores it in a session store and sends back the session id. This session id gets stored by the browser in a cookie which then gets sent on each request to the server for validation.

### Token-based

Instead of using cookies, tokens are used for this method of authentication. Once a user authenticates, the server returns a signed token. Subsequent requests send this token (usually in the `Authorization` header) which is validated (not stored, hence no database lookup is needed) by the server. `JWT` is the most commonly used token. The token consists of:

- Header (token type and hashing algorithm)
- Payload (statements about an entity, in this case, the user)
- Signature (to verify that the message hasn't been tampered with)

All of the above are base64 encoded, concatenated (`.`) and hashed. 

### OAuth (authorization)

OAuth is a standard that allows to authorize access to resources without providing credentials. Companies such as Amazon, Facebook, Google etc allow users to share their information with third party applications.

### OpenID

- 

### SAML (security assertion markup language tokens)

- 

### API token
 
-  

### API authentication

- API Keys - uniquely generated key for each user
- Bearer token - gets generated on the server in response to a login and stored against a user id

## References

- [HTTP Authentication: Basic and Digest Access Authentication](https://datatracker.ietf.org/doc/html/rfc2617)
- [Basic and Digest Authentication Types](https://blog.wildix.com/basic-digest-authentication/)
- [Web Authentication Methods Compared](https://testdriven.io/blog/web-authentication-methods/#token-based-authentication)
