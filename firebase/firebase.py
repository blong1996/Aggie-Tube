import pyrebase

config = {
  "apiKey": "AIzaSyBCJqPcs8VvaLdlHd-J5SdMIOXu1NvwFns",
  "authDomain": "aggie-tube.firebaseapp.com",
  "databaseURL": "https://aggie-tube.firebaseio.com",
  "projectId": "aggie-tube",
  "storageBucket": "aggie-tube.appspot.com"
}

firebase = pyrebase.initialize_app(config)


# Get a reference to the auth service
auth = firebase.auth()

# Get a reference to the database service
db = firebase.database()
# users
all_users = db.child("users").get()
userObj = {}
user = None


def login(email, password):
    # Log the user in
    userExists = False
    global userObj
    global user
    if all_users.each():
        for userl in all_users.each():
            if email == userl.val()['email']:
                user = auth.sign_in_with_email_and_password(email, password)
                print("Login successful! User info:\n")
                displayUser(user)
                userObj = userl.val()
                userExists = True
    if not userExists:
        print("User does not exist with email: {}".format(email))
    return userExists


def refreshUserToken():
    # before the 1 hour expiry:
    global user
    user = auth.refresh(user['refreshToken'])


def createUser(email, password):
    global user
    user = auth.create_user_with_email_and_password(email, password)

    global userObj

    if user:
        username = ""
        for letter in email:
            if letter == '@':
                break
            username += letter
        user["displayName"] = username
        newUser = {
            "email": email,
            "username": username
        }
        db.child("users").child(username).set(newUser)
        print("User creation successful! User info:\n")
        displayUser(user)

        userObj = newUser
    return user


def emailVerification():
    auth.send_email_verification(user['idToken'])


def currentUser():
    refreshUserToken()
    global user
    user = auth.current_user
    return user


def getAccountInfo():
    refreshUserToken()
    return auth.get_account_info(user['idToken'])


def getFriends():
    refreshUserToken()
    friends = db.child("users").child(userObj["username"]).child("friends").get()
    return friends

def addFriend(friend):
    refreshUserToken()
    db.child("users").child(userObj["username"]).child("friends").child(friend['username']).set(friend)

def getFriend(friendName):
    refreshUserToken()
    return db.child("users").child(userObj["username"]).child("friends").child(friendName).get()


def getPlaylists():
    refreshUserToken()
    return db.child("users").child(userObj["username"]).child("playlists").get()


def addToFavs(video):
    refreshUserToken()
    db.child("users").child(userObj["username"]).child("playlists").child("MyFav").child(video['id']).set(video)

def getPlaylist(playlistName):
    refreshUserToken()
    return db.child("users").child(userObj["username"]).child("playlists").child(playlistName).get()



def displayUser(user):
    refreshUserToken()
    print("{")
    for key in user:
        print("    {} : {}".format(key, user[key]))
    print("}")


def logout():
    global userObj
    global user
    userObj = {}
    user = {}
    print("User has been logged out")