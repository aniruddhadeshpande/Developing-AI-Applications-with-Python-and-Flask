# Flask Request and Response Objects

## Overview

Flask provides powerful **Request** and **Response** objects for handling HTTP communication between clients and servers. These objects allow developers to access request data, customize responses, and control HTTP behavior effectively.

## Flask Routes Configuration

### Basic Route Setup
- Routes are defined using the `@app.route` decorator
- **Default method**: GET (implicit)
- **Custom methods**: Specify using the `methods` parameter

### Examples

```python
# Implicit GET method
@app.route('/users')
def get_users():
    return "Users list"

# Explicit GET method
@app.route('/users', methods=['GET'])
def get_users_explicit():
    return "Users list"

# Multiple methods
@app.route('/health', methods=['GET', 'POST'])
def health_check():
    if request.method == 'GET':
        return {"status": "OK", "method": "GET"}
    elif request.method == 'POST':
        return {"status": "OK", "method": "POST"}
```

## Flask Request Object

### Core Attributes

| Attribute | Description |
|-----------|-------------|
| `server` | Server address as tuple (host, port) |
| `headers` | HTTP headers sent with request |
| `url` | Complete URL of the requested resource |
| `access_route` | List of IP addresses for forwarded requests |
| `full_path` | Complete request path including query strings |
| `is_secure` | Boolean - True for HTTPS/WSS protocols |
| `is_json` | Boolean - True if request contains JSON data |
| `cookies` | Dictionary of cookies sent with request |

### Header Information Access

**Available header data**:
- `cache_control` - Browser caching information
- `accept` - Content types understood by client
- `accept_encoding` - Content encoding preferences
- `user_agent` - Client identification (browser, OS, version)
- `accept_language` - Language and locale preferences
- `host` - Host and port number of requested server

### Request Data Access Methods

#### Raw Data Methods
- `get_data()` - Access POST request data as bytes (requires manual parsing)
- `get_json()` - Parse JSON data from POST request automatically

#### Focused Data Access Methods
- `args` - Query parameters as dictionary
- `json` - Parsed JSON data as dictionary
- `files` - User uploaded files
- `form` - Form submission values
- `values` - Combined args and form data

### Data Extraction Examples

```python
from flask import Flask, request

@app.route('/course')
def get_course():
    # Using indexing (throws 400 error if missing)
    course = request.args['course']
    
    # Using get method (returns None if missing)
    rating = request.args.get('rating')
    
    return f"Course: {course}, Rating: {rating}"
```

**URL Example**: `http://localhost:5000/course?course=Capstone&rating=10`

### Data Structure Types
Request methods return:
- **Multidict**
- **Immutable Multidict**  
- **Combined Multidict**

All behave like Python dictionaries and support indexing or `.get()` method for value extraction.

## Flask Response Object

### Response Attributes

| Attribute | Description |
|-----------|-------------|
| `status_code` | HTTP status indicating success/failure |
| `headers` | Additional response information |
| `content_type` | Media type of requested resource |
| `content_length` | Size of response message body |
| `content_encoding` | Encoding applied to response |
| `mimetype` | Media type of response |
| `expires` | Expiration date/time for response |

### Response Methods

| Method | Purpose |
|--------|---------|
| `set_cookie()` | Set browser cookie on client |
| `delete_cookie()` | Remove cookie from client |

### Response Creation Methods

#### Automatic Response Creation
```python
# Automatic response with 200 status and HTML MIME type
@app.route('/users')
def users():
    return "<h1>Users Page</h1>"

# JSONify creates response automatically
@app.route('/api/data')
def api_data():
    return jsonify({"message": "success"})
```

#### Custom Response Creation
```python
from flask import make_response, redirect, abort

# Custom response
@app.route('/custom')
def custom_response():
    response = make_response("Custom content", 201)
    response.headers['Custom-Header'] = 'Value'
    return response

# Redirect (302 status)
@app.route('/old-url')
def redirect_example():
    return redirect('/new-url')

# Error response
@app.route('/restricted')
def restricted():
    abort(403)  # Forbidden
```

## Practical Example

### Server Information Display
When a client makes a request, you can access detailed information:

```python
@app.route('/debug')
def debug_request():
    info = {
        'server': '127.0.0.1:5000',
        'host': request.headers.get('Host'),
        'user_agent': request.headers.get('User-Agent'),
        'url': request.url,
        'access_route': list(request.access_route),
        'full_path': request.full_path,
        'is_json': request.is_json,
        'is_secure': request.is_secure,
        'cookies_count': len(request.cookies)
    }
    return jsonify(info)
```

## Key Takeaways

1. **Request Object**: Flask automatically creates a request object for every HTTP call, containing comprehensive information about the client request
2. **Data Access**: Multiple methods available for accessing different types of request data (query params, JSON, form data, files)
3. **Response Control**: Response objects allow setting custom status codes, headers, cookies, and content types
4. **Error Handling**: Use `.get()` method for safe parameter access to avoid 400 errors
5. **Automatic vs Custom**: Flask creates responses automatically, but custom responses provide greater control over HTTP behavior

Flask's request and response objects provide a comprehensive foundation for building robust web applications with full control over HTTP communication.