from youtube.youtube_videos import youtube_search
import json

# test = youtube_search("spinners")
# vid1 = test[1][00]
# print("Title: " + vid1['snippet']['title'] +
#       " Thumbnail: " + vid1['snippet']['thumbnails']['high']['url'] +
#       " Channel: " + vid1['snippet']['channelTitle'] +
#       " Video:  https://www.youtube.com/watch?v=" + vid1['id']['videoId']
#       )
# just_json = test[1]
# for video in just_json:
#     print(video['snippet']['title'])

video_dict = {'youID': [], 'title': [], 'pub_date': []}


def get_top_vids(query):
    search = youtube_search(query, 50)
    videos = []

    for vid in search[1]:
        vid_dic = {
            'title': vid['snippet']['title'],
            'thumbnail': vid['snippet']['thumbnails']['high']['url'],
            'channel': vid['snippet']['channelTitle'],
            'url': 'https://www.youtube.com/watch?v=' + vid['id']['videoId'],
            'id': vid['id']['videoId']
        }
        videos.append(vid_dic)
    return videos


def grab_videos(keyword, token=None):
    res = youtube_search(keyword)
    token = res[0]
    videos = res[1]
    for vid in videos:
        video_dict['youID'].append(vid['id']['videoId'])
        video_dict['title'].append(vid['snippet']['title'])
        video_dict['pub_date'].append(vid['snippet']['publishedAt'])
    print("added " + str(len(videos)) + " videos to a total of " + str(len(video_dict['youID'])))
    return token

    # token = grab_videos("spinners")
    # while token != "last_page":
    #     token = grab_videos("spinners", token=token)
