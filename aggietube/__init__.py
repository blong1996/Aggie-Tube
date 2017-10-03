from flask import Flask, render_template, request

from youtube_tutorial.youtube import get_top_vids

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        videos = get_top_vids(request.form['query'])

    else:
        videos = get_top_vids('')

    return render_template('index.html', videos=videos)


@app.route('/<query>', methods=['POST'])
def search(query):
    videos = get_top_vids(query)

    return render_template('index.html', videos=videos)


if __name__ == '__main__':
    app.run()
