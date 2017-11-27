# Import flask dependencies
from flask import Blueprint, render_template, request

from youtube.youtube import get_top_vids
import firebase.firebase as firebase

aggie_tube = Blueprint('app', __name__)

user = firebase.user

@aggie_tube.route('/friends', methods=['GET', 'POST'])
def friends():
    user = firebase.userObj
    friends = {}
    if user:
        friends = firebase.getFriends()
    if not friends:
        friends = {}

    return render_template('friends.html', friends=friends, user=user)


@aggie_tube.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form['email']:
        if not firebase.login(request.form['email'], request.form['password']):
            firebase.createUser(request.form['email'], request.form['password'])

        videos = get_top_vids('')
    elif request.method == 'POST' and request.form['query']:
        videos = get_top_vids(request.form['query'])
    else:
        videos = get_top_vids('')
    user = firebase.userObj
    return render_template('index.html', videos=videos, user=user)


@aggie_tube.route('/<query>', methods=['GET', 'POST'])
def search(query):
    videos = get_top_vids(query)

    return render_template('index.html', videos=videos)


@aggie_tube.route('/play/<string:vidId>', methods=['GET'])
def play_video(vidId):
    return render_template('play_video.html', vidId=vidId)


@aggie_tube.route('/login', methods=['GET'])
def login():
    firebase.logout()
    return render_template('login.html')


@aggie_tube.route('/friends/<string:userName>/<string:friend>', methods=['GET'])
def viewFriend(userName, friend):
    user = firebase.userObj
    friend = firebase.getFriend(friend)

    return render_template('profile.html', user=user, friend=friend)


@aggie_tube.route('/playlists', methods=['GET', 'POST'])
def playlists():
    user = firebase.userObj
    playlists = {}
    if user:
        playlists = firebase.getPlaylists()
    if not playlists:
        playlists = {}

    return render_template('playlists.html', playlists=playlists, user=user)


@aggie_tube.route('/playlist', methods=['GET', 'POST'])
def openList():
    user = firebase.userObj
    list = firebase.getPlaylist("MyFav")

    if request.method == 'POST':
        vid_dic = {
            'title': request.form['title'],
            'thumbnail': request.form['thumbnail'],
            'channel': request.form['channel'],
            'id': request.form['vidId']
        }
        firebase.addToFavs(vid_dic)

    return render_template('playlist.html', user=user, list=list)