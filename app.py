from flask import Flask, request, jsonify, make_response, redirect,abort
import requests

app = Flask(__name__)

# Mock database for demonstration
books_db = {
    "9780345391803": {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "isbn": "9780345391803"
    },
    "9780061120084": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780061120084"
    }
}

# ============================================
# 1. BASIC ROUTES WITH DIFFERENT HTTP METHODS
# ============================================

@app.route('/')
def home():
    """Basic home route returning HTML"""
    return '<h1>Flask Dummy Project - Learning API Development</h1>', 200

@app.route('/health', methods=['GET','POST'])

def health():
    """Route that responds to both GET and POST requests"""
    if request.method == 'GET':
        return jsonify({
            'status':'ok',
            'method':'GET'
        }),200
    elif request.method == 'POST':
        return jsonify({
            'status':'ok',
            'method': 'POST'
        }),200

# ============================================
# 2. REQUEST OBJECT EXAMPLES
# ============================================

@app.route('/request-info')
def request_info():
    """Display various request object attributes"""
    info = {
        'server': f"{request.server[0]}:{request.server[1]}",
        'host': request.headers.get('host'),
        'user_agent': request.headers.get('User-Agent'),
        'url': request.url,
        'access_route': list(request.access_route),
        'full_path': request.full_path,
        'is_json': request.is_json,
        'is_secure': request.is_secure,
        'cookie_count': len(request.cookies)
    }

    return jsonify(info), 200

@app.route('/query-params')
def query_params():
    """Extract query parameters from URL"""
    # Example: /query-params?course=Capstone&rating=10
    
    # Using indexing (raises error if parameter missing)
    # course = request.args['course']

    # Using get method (returns None if missing) - safer
    course = request.args.get('course', 'Not Provided')
    ratings = request.args.get('ratings', 'Not Provided')

    return jsonify({
        'course': course,
        'ratings': ratings,
        'all_params': dict(request.args)
    }),200

@app.route('/submit-form',methods=['POST'])
def submit_form():
    """Handle form data submission"""
    # Get form data

    name = request.form.get('name')
    email = request.form.get('email')

    # Get JSON data if sent
    if request.is_json:
        data = request.get_json()
        return jsonify({
            'message': 'JSON data received',
            'data': data
        }),201

    return jsonify({
        'message': 'Data Received',
        'name': name,
        'email': email
    }),201

# ============================================
# 3. DYNAMIC ROUTES WITH TYPE CONVERTERS
# ============================================

@app.route('/book/<string:isbn>')
def get_book_by_isbn_string(isbn: str):
    """Get book by ISBN (string parameter)"""
    book = books_db.get(isbn)

    if book:
        return jsonify(book), 200
    else:
        return jsonify({'error':'Book not found'}), 404


@app.route('/user/<uuid:user_id>')
def get_user_id(user_id):
    """Get user by UUID"""
    return jsonify({
        'user_id': str(user_id),
        'message': f"Fetching user id with {user_id}"
    }), 200


# ============================================
# 4. EXTERNAL API CALLS
# ============================================

@app.route('/external/author/<string:author_name>')
def search_author(author_name):
    """Call external OpenLibrary API to search for author"""
    try:
        url = f'https://openlibrary.org/search/authors.json?q={author_name}'
        response = requests.get(url, timeout = 5)
        
        if response.status_code == '200':
            return jsonify(response.json()),200
        elif response.status_code == '400':
            return jsonify({'error': 'Resourse not available'}), 404
        else:
            return jsonify({'error': 'Something went wrong'}), 500
    except response.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

# ============================================
# 5. RESPONSE OBJECT CUSTOMIZATION
# ============================================

@app.route('/custom-response')
def custom_response():
    """Create custom response with specific attributes"""
    response = make_response(
        jsonify({
            'message': 'Custom response created'
        }), 200
    )

    response.headers['X-Custom-Header'] = 'CustomValue'
    response.headers['Content-Type'] = 'application/json'
    response.set_cookie('session_id', '1234567')
    return response

@app.route('/redirect-example')
def redirect_example():
    """Redirect to another route"""
    return redirect('/health', code=302)

@app.route('/abort-example/<int:code>')
def abort_example(code):
    """Example of using abort"""
    if code >=400:
        abort(code)

    return jsonify({'message': 'Success'}), 200

# ============================================
# 7. APPLICATION-LEVEL ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'API not found',
        'message': 'The requested resource does not exist'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Something went wrong on the server',
        'message': 'Internal server error'
    }), 500
@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors"""
    return jsonify({
        'error': 'Bad request',
        'message': 'The request contains invalid parameters'
    }), 400

@app.errorhandler(401)
def unauthorized(error):
    """Handle 401 errors"""
    return jsonify({
        'error': 'Unauthorized',
        'message': 'Credentials are missing or invalid'
    }), 401

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )