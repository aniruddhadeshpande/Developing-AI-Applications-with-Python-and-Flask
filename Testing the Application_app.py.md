## Testing the Application

Here are curl commands to test various endpoints:

```bash
# 1. Test basic home route
curl http://localhost:5000/

# 2. Test health endpoint with GET
curl http://localhost:5000/health

# 3. Test health endpoint with POST
curl -X POST http://localhost:5000/health

# 4. Test request info
curl http://localhost:5000/request-info

# 5. Test query parameters
curl "http://localhost:5000/query-params?course=Capstone&ratings=10"

# 6. Test form submission with JSON
curl -X POST http://localhost:5000/submit-form \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# 7. Test dynamic route with ISBN
curl http://localhost:5000/book/9780345391803

# 8. Test dynamic route with integer
curl http://localhost:5000/book/123

# 9. Test UUID route
curl http://localhost:5000/user/550e8400-e29b-41d4-a716-446655440000

# 10. Test path parameter
curl http://localhost:5000/path/users/profile/settings

# 11. Test airport terminals
curl http://localhost:5000/terminals/SFO

# 12. Test external API - author search
curl http://localhost:5000/external/author/Michael%20Crichton

# 13. Test search with query parameter
curl "http://localhost:5000/search?q=user1"

# 14. Test search without parameter (422 error)
curl http://localhost:5000/search

# 15. Test search with non-existent resource (404 error)
curl "http://localhost:5000/search?q=user999"

# 16. Test resource creation
curl -X POST http://localhost:5000/create-resource \
  -H "Content-Type: application/json" \
  -d '{"name": "New Item", "description": "Test item"}'

# 17. Test custom response
curl -v http://localhost:5000/custom-response

# 18. Test redirect
curl -L http://localhost:5000/redirect-example

# 19. Test 404 error
curl http://localhost:5000/nonexistent-route

# 20. Test all HTTP methods
curl http://localhost:5000/test-all-methods
curl -X POST http://localhost:5000/test-all-methods
curl -X PUT http://localhost:5000/test-all-methods
curl -X DELETE http://localhost:5000/test-all-methods
```

## Key Concepts Demonstrated

### Error Handling

- HTTP status codes: 200, 201, 204, 400, 401, 403, 404, 422, 500
- Application-level error handlers using `@app.errorhandler()`
- Explicit status code returns using tuples
- Using `make_response()` for custom responses
- Using `abort()` to trigger error responses

### Request and Response Objects

- Accessing request attributes (server, headers, URL, etc.)
- Extracting query parameters with `request.args`
- Handling form data with `request.form`
- Parsing JSON data with `request.get_json()`
- Customizing response headers and cookies
- Using `jsonify()` for JSON responses
- Implementing redirect with `redirect()`

### Dynamic Routes

- String parameters: `<string:variable>`
- Integer parameters: `<int:variable>`
- UUID parameters: `<uuid:variable>`
- Path parameters: `<path:variable>`
- Calling external APIs using the `requests` library
- Processing and forwarding API responses

This complete Flask application integrates all the concepts from your transcripts and provides a solid foundation for building RESTful APIs.[1][2][3][4]

***

## Common Mistake: `request` Not Defined

If you see `"request showing not defined"` for code like:

```python
if request.method == 'GET':
```

You must import `request` from Flask. The import should look like:

```python
from flask import Flask, request
```

A working example:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/health', methods=['GET', 'POST'])
def health():
    if request.method == 'GET':
        return 'GET method received'
    elif request.method == 'POST':
        return 'POST method received'
```

Make sure you add `request` to your Flask import at the top of your file to use it correctly in your routes.[2]

[1](https://hexmos.com/freedevtools/c/python-flask/basic-hello-world/)
[2](https://www.geeksforgeeks.org/python/how-to-write-a-simple-flask-api-for-hello-world/)
[3](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
[4](https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/)