from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home/')
@app.route('/aggietube/')
@app.route('/')
def main(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run()