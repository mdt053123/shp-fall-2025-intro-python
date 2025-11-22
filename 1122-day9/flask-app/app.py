from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return "<h1>Michael's Website</h1>"

@app.post('/double')
def double():
    n_str = request.form['num']
    n = float(n_str)

    result = n * 2
    return render_template("result.html", original_number=n, result=result)

@app.route('/double-number')
def double_number():
    return render_template("double_number.html")


app.run(debug=True)