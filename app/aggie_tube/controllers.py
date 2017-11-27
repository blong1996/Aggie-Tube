# Import flask dependencies
from flask import Blueprint, render_template, request
import youtube.youtube as youtube
import firebase.firebase as firebase

aggie_tube = Blueprint('app', __name__)

user = firebase.user

@aggie_tube.route('/friends', methods=['GET', 'POST'])
def friends():
    user = firebase.userObj
    friends = {}
    if user:
        friends = firebase.getFriends()
        try:
            for friend in friends.each():
                print(friend)
        except Exception as e:
            print(e)
            friends = {}

    return render_template('friends.html', friends=friends, user=user)


@aggie_tube.route('/', methods=['GET', 'POST'])
def home():
    try:
        if request.method == 'POST' and request.form['email']:
            if not firebase.login(request.form['email'], request.form['password']):
                firebase.createUser(request.form['email'], request.form['password'])

            videos = youtube.get_top_vids('')
    except Exception as e:
        print("Error {}".format(e))
        try:
            if request.method == 'POST' and request.form['query']:
                videos = youtube.get_top_vids(request.form['query'])
        except Exception as e:
            print("Error {}".format(e))
            videos = youtube.get_top_vids('')

    if request.method == 'GET':
        videos = youtube.get_top_vids('')
    user = firebase.userObj
    return render_template('index.html', videos=videos, user=user)


@aggie_tube.route('/<query>', methods=['GET', 'POST'])
def search(query):
    videos = youtube.get_top_vids(query)
    user = firebase.userObj

    return render_template('index.html', videos=videos, user=user)


@aggie_tube.route('/play/<string:vidId>', methods=['GET'])
def play_video(vidId):
    user = firebase.userObj
    return render_template('play_video.html', vidId=vidId, user=user)


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
        try:
            for list in playlists.each():
                print(list)
        except Exception as e:
            print(e)
            playlists = {}

    return render_template('playlists.html', playlists=playlists, user=user)


@aggie_tube.route('/playlist/<string:title>', methods=['GET', 'POST'])
def openList(title):
    user = firebase.userObj


    if request.method == 'POST':
        video = youtube.get_video(title)
        firebase.addToFavs(video)
    list = firebase.getPlaylist("MyFav")
    return render_template('playlist.html', user=user, list=list)


@aggie_tube.route('/users', methods=['GET'])
def viewUsers():
    users = firebase.allUsers()
    user = firebase.userObj
    try:
        for user in users.each():
            print(user)
        return render_template('friends.html', friends=friends, user=user)
    except Exception as e:
        print(e)
        videos = youtube.get_top_vids('')
        return render_template('index.html', videos=videos, user=user)


