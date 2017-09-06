from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home/')
@app.route('/aggietube/')
def hello(name=None):
    return render_template('index.html', name=name)
if __name__ == '__main__':
    app.run()
