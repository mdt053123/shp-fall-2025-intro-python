# Day 9: Web Development with Flask

## Topics Covered

### 1. Flask Basics
Flask is a lightweight web framework for Python.

```python
from flask import Flask, render_template, request

app = Flask(__name__)
```

### 2. Routes & Decorators
Routes define URL endpoints.

```python
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return "<h1>About Page</h1>"
```

### 3. HTML Templates
Templates are stored in the `templates/` folder.

```
flask-app/
├── app.py
└── templates/
    ├── index.html
    └── result.html
```

#### Rendering Templates
```python
return render_template("index.html")
```

### 4. Template Variables (Jinja2)
Pass data from Python to HTML.

```python
return render_template("result.html", 
                       original_number=n, 
                       result=n*2)
```

In HTML:
```html
<div>{{ original_number }} × 2 = {{ result }}</div>
```

### 5. Handling Form Data

#### HTML Form
```html
<form action="/double" method="post">
    <input type="number" name="num">
    <button type="submit">Submit</button>
</form>
```

#### Flask Route
```python
@app.post('/double')
def double():
    n_str = request.form['num']
    n = float(n_str)
    result = n * 2
    return render_template("result.html", 
                           original_number=n, 
                           result=result)
```

### 6. CSS Styling
Style your pages with CSS in `<style>` tags or external files.

```html
<style>
    body {
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #667eea, #764ba2);
    }
    .container {
        background: white;
        border-radius: 20px;
        padding: 50px;
    }
</style>
```

### 7. Running the App
```python
app.run(debug=True)
```

Access at `http://localhost:5000`

## Project Structure
```
flask-app/
├── app.py              # Main application
└── templates/
    ├── index.html      # Home page
    ├── double_number.html  # Input form
    └── result.html     # Results display
```

## Key Concepts
- **Route** - URL path that triggers a function
- **Template** - HTML file with dynamic content
- **Form** - User input that gets sent to server
- **POST** - HTTP method for submitting data
- **GET** - HTTP method for requesting pages

