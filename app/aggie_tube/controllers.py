# Import flask dependencies
from flask import Blueprint, render_template, request

from youtube.youtube import get_top_vids
aggie_tube = Blueprint('app', __name__)


@aggie_tube.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        videos = get_top_vids(request.form['query'])

    else:
        videos = get_top_vids('')

    return render_template('index.html', videos=videos)


@aggie_tube.route('/<query>', methods=['POST'])
def search(query):
    videos = get_top_vids(query)

    return render_template('index.html', videos=videos)


