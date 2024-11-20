# Jacob Jam
This is a playground repository to test and demo Jacob.

## Flask Application Structure

This application is built using Flask, a lightweight WSGI web application framework. It follows a modular structure using Flask Blueprints for organizing routes and templates.

### Routes Organization

Routes are defined in `/app/main/routes.py` using Flask Blueprints. The main blueprint is initialized in `/app/main/__init__.py`:

from flask import Blueprint
bp = Blueprint('main', __name__)

Current routes in the application:

- **Root Route ('/')**
  - Methods: GET, POST
  - Handler: `index()`
  - Template: `index.html`
  - Purpose: Renders the main page

- **Favicon Route ('/favicon.ico')**
  - Methods: GET
  - Handler: `favicon()`
  - Purpose: Serves the site favicon

### Templates Usage

Templates are stored in the `/app/templates/` directory and are rendered using Flask's `render_template` function. The application uses Jinja2 templating engine for dynamic content rendering.

Current templates:
- `index.html` - Main page template
- `404.html` - Not found error page
- `500.html` - Internal server error page

### Adding a New Route and Template

To add a new route and template to the application:

1. Create a new template file in `/app/templates/`:
   <!-- /app/templates/new_page.html -->
   {% extends "base.html" %}
   {% block content %}
     <!-- Your template content here -->
   {% endblock %}

2. Add a new route in `/app/main/routes.py`:
   @bp.route('/new-page', methods=['GET'])
   def new_page():
       return render_template('new_page.html', title='New Page')

### Best Practices

1. **Route Naming**
   - Use lowercase for route URLs
   - Separate words with hyphens
   - Keep URLs descriptive but concise

2. **Template Organization**
   - Use template inheritance with base.html
   - Keep templates in the appropriate directory
   - Use meaningful template names

3. **Route Implementation**
   - Always specify allowed HTTP methods
   - Include appropriate error handling
   - Pass necessary context to templates

4. **Error Handling**
   - Custom error pages are handled through error handlers
   - Error templates should extend the base template
   - Include helpful error messages and navigation options