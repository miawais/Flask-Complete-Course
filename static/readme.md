# Static Directory

The `static` directory in a Flask project is used to store static files such as CSS, JavaScript, images, and other assets that do not change dynamically. It helps in organizing and serving static content efficiently.

- **Purpose**: To store static files.
- **Path**: Typically located at the root level of the Flask project.
- **Access**: Static files can be accessed in templates using `url_for('static', filename='path/to/file')`.
- **Example**: If you have a CSS file `style.css` in `static/css`, you can link to it in an HTML template as follows:
  ```html
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
