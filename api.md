# API docs

Conventions used in this document:

- `<linkely>` - the linkely API endpoint, for the current public version: `https://linkely.co/v1`
- `[something]` - a generic placeholder

**Note:** When an API path ends with a `/`, it's usually mandatory.


## Authorized calls

Autorized API calls are made using JWT tokens.

### Authenticate

Authenticated calls to the API are made by sending a JWT token in the
header of the request.

### `POST /token/` Generate token using username/password

Tokens are returned by the `POST /token` endpoint.

Request:
```
POST <linkely>/token/
{
  "username": "[username]",
  "password": "[password]"
}
```

Response:
```
{
  "access": "[access token]",
  "refresh": "[refresh token]"
}
```

### Using the access token

To use the access token to authenticate a call to the API, simply set
the `Authorization` header to `Bearer [access token]`.

[httpie][httpie] example:
```
http linkely.co/v1/articles/ 'Authorization:Bearer [access token]'
```

curl example:
```
curl http://localhost:8080/v1/articles/ -H "Authorization: Bearer [access token]"
```


### `POST /token/refresh/` Refreshing the access token

The access token has a limited lifetime, so it has to be refreshed at
regular intervals. To get a new access token using the refresh token
returned by `POST /token` above, use the `POST /token/refresh`
endpoint:


Request:
```
POST <linkely>/token/refresh/
{
  "refresh": "[refresh token]"
}
```

Response:
```
{
  "access": "[access token]"
}
```

## `GET /articles/` List articles

List all articles.

*Requires authentication*

Request:
```
GET <linkely>/articles/
```

Response:
```
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 23,
      "url": "https://www.dn.se/sverige/jagare-skot-fel-djur-far-bota-3-500/",
      "title": "Älgko skjuten av misstag – jägare trodde det var vildsvin",
      "date": "2021-01-02T20:50:31.243524Z",
      "user": {
        "id": 3,
        "username": "andre"
      }
    }
  ]
}
```


[httpie]: https://httpie.io/
