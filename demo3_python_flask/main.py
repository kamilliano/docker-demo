from flask import render_template

from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return "hello go to route=/hello"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)