# Templates Directory

The `templates` directory in a Flask project is used to store HTML template files. These templates are rendered and served by Flask routes, allowing dynamic content generation.

- **Purpose**: To store HTML template files.
- **Path**: Typically located at the root level of the Flask project.
- **Access**: Templates are rendered using `render_template('template_name.html', context_variable=value)`.
- **Example**: If you have an HTML file `index.html` in `templates`, you can render it in a route as follows:
  ```python
  @app.route('/')
  def home():
      return render_template('index.html', title='Home')
