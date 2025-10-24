# Summary: Introduction to Flask

This session provides a comprehensive introduction to **Flask**, a lightweight Python micro web framework, covering its features, installation, dependencies, extensions, and comparison with Django.

## What is Flask?

**Flask** is a micro web framework for Python that enables developers to create web applications quickly and efficiently. It is:
- **Not opinionated:** Does not enforce specific tools or structures
- **Lightweight:** Ships with minimal dependencies
- **Extensible:** Supports numerous community extensions for added functionality

### History
- Created in **2004** by **Armin Ronacher** as an April Fool's joke
- Quickly gained popularity for ease of use and extensibility
- Current version: **Flask 2.2.2** (requires Python 3.7+)

## Main Features of Flask

### Core Features
- **Development Web Server:** Runs applications in development mode
- **Debugger:** Interactive traceback and stack traces displayed in browser
- **Logging:** Uses standard Python logging for application and custom logs
- **Testing Support:** Enables test-driven development (TDD) with frameworks like PyTest and coverage
- **Request/Response Objects:** Direct access to pull arguments and customize responses

### Additional Features
- **Static Assets:** Support for CSS, JavaScript files, and images with template tags
- **Dynamic Pages:** Uses **Jinja templating framework** to display changing information and check user login status
- **Routing:** Supports dynamic URLs for RESTful services, multiple HTTP methods, and redirection
- **Error Handling:** Global error handlers at the application level
- **Session Management:** Built-in user session management

## Popular Community Extensions

Flask's functionality can be significantly expanded through community extensions:

| Extension | Purpose |
|-----------|---------|
| **Flask-SQLAlchemy** | Adds ORM support for working with database objects in Python |
| **Flask-Mail** | Sets up SMTP mail server capabilities |
| **Flask-Admin** | Easily adds admin interfaces to applications |
| **Flask-Uploads** | Customized file uploading functionality |
| **Flask-CORS** | Handles Cross-Origin Resource Sharing for JavaScript requests |
| **Flask-Migrate** | Database migrations for SQLAlchemy ORM |
| **Flask-User** | User authentication, authorization, and management |
| **Marshmallow** | Object serialization and deserialization |
| **Celery** | Powerful task queue for background tasks and complex scheduling |

## Installation

Flask is available via **pip** (Python package manager):

```bash
# Recommended: Create virtual environment first
python -m venv myenv

# Install Flask (version pinning recommended)
pip install Flask==2.2.2
```

**Best Practice:** Pin version numbers to ensure reproducibility across development, staging, and production environments, and prevent issues from automatic updates.

## Built-in Dependencies

Flask includes several key dependencies that power its features:

| Dependency | Function |
|------------|----------|
| **Werkzeug** | Implements WSGI (Web Server Gateway Interface) - standard Python interface between applications and servers |
| **Jinja** | Template language for rendering application pages |
| **MarkupSafe** | Comes with Jinja; escapes untrusted input to prevent injection attacks |
| **ItsDangerous** | Securely signs data to detect tampering; protects Flask session cookies |
| **Click** | Framework for command-line applications; provides Flask command and custom management commands |

Use `pip freeze` in your virtual environment to view all installed built-in packages.

## Flask vs. Django

| Aspect | Flask | Django |
|--------|-------|--------|
| **Framework Type** | Micro framework (lightweight) | Full-stack framework |
| **Dependencies** | Minimal - only basic requirements included | Comprehensive - everything needed for full-stack apps |
| **Flexibility** | Very flexible - plug-and-play architecture | Opinionated - makes most decisions for developers |
| **Extensibility** | Developer chooses extensions as needed | Includes built-in features out of the box |
| **Approach** | Unopinionated | Opinionated - focuses developer on application logic |

## Key Takeaways

- Flask is a **micro framework** with minimal dependencies, ideal for developers who want control and flexibility
- It includes essential features for web development: **debugging, routing, templates, and error handling**
- Flask is highly **extensible** through community extensions that add specialized functionality
- Installation is simple via **pip**, with virtual environment usage recommended
- Compared to Django, Flask is **lighter and more flexible**, while Django is a **full-stack solution** with built-in features