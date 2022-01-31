The answer to the second part of the challenge is within this note. Most of these thoughts are not implemented as the instruction was to not implementing but to just pointing them out. If you had any questions or doubts, I would be more than happy to have a techie chit-chat! :)

* Suggestions for the API improvement:
    - `rates` is a more suitable name for this endpoint. if an endpoint
      returns a `collection of results` it should be named in a plural format
      based on REST Resource Naming Guide.
    - Making the `/rate` endpoint a `GET` request instead of a `POST` request;
      In the context of REST APIs, whenever making multiple identical requests
      has the same effect as making a single request — then that REST API is
      `idempotent`. An HTTP method is idempotent if an identical request can be
      made once or several times in a row with the same effect while leaving the
      server in the `same state`. Since our endpoint is not altering any state
      inside the server, and just doing a simple calculation, it would be an
      improvement to make the method a GET request. Now, because of the 
      idempotency of a GET request, most of the webpage resources are returned
      via this method, and the browser by default will cache get requests.
      POST is not Idempotent and can’t be cached on the client-side.
    - using API versioning is a step toward improvement, so it would be 
      better if we add a `/api/v1` prefix to the main route.
    - Not using `trailing forward` slash in URIs, as the last character within
      a URI’s path, a forward slash (/) adds no semantic value and may cause
      confusion. It’s better to drop them completely.