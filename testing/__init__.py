import unittest
from test import support
import firebase.firebase as fb

class TestFirebase(unittest.TestCase):
    print("Beginning Firebase Tests\n\n")
    # Only use setUp() and tearDown() if necessary

    # def setUp(self):
    #     ... code to execute in preparation for tests ...
    #
    # def tearDown(self):
    #     ... code to execute to clean up after tests ...



    def test_get_friends(self):
        print("\n getFriends() Test: \n")
        friends = fb.getFriends()
        if not friends:
            print("Friends Test Failed")
        else:
            print(friends.each())

    def test_get_playlists(self):
        print("\n getPlaylists() Test: \n")
        playlists = fb.getPlaylists()
        if not playlists:
            print("Playlists Test Failed")
        else:
            print(playlists.each())

    def test_fb(self):
        print("\nlogin() Test: \n")
        user = fb.login('bllong@aggies.ncat.edu', '123456')
        if not user:
            print("Login Test Failed, user not yet ")

        print("\n getPlaylists() Test: \n")
        playlists = fb.getPlaylists()
        if not playlists:
            print("Playlists Test Failed")
        else:
            print(playlists.each())


    # def test_feature_two(self):
        #Test feature two.

#
# class MyTestCase2(unittest.TestCase):
#     # ... same structure as MyTestCase1 ...
#
# # ... more test classes ...

def test_main():
    support.run_unittest(TestFirebase)

if __name__ == '__main__':
    test_main()