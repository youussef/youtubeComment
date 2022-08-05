
from requests import request
import requests
from google_apis import create_service
import time

CLIENT_FILE = 'client-secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = [
	'https://www.googleapis.com/auth/youtube',
	'https://www.googleapis.com/auth/youtube.force-ssl',
	'https://www.googleapis.com/auth/youtubepartner'
]

service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

#make sure to put your api key here

ApiKey=""
YoutubeChannel = "" 
comment  = "this is a first comment give me the 10K"

#get the last two videos from the channel 

jsondata = requests.get("https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId="+YoutubeChannel+"&maxResults=2&key="+ApiKey)

latestVideo=(jsondata.json().get('items')[0].get('id').get('videoId'))
newvideo=latestVideo
#check if there is a new video
while(newvideo==latestVideo):
    
	jsondata = requests.get("https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId="+YoutubeChannel+"&maxResults=2&key="+ApiKey)
	latestVideo=(jsondata.json().get('items')[0].get('id').get('videoId'))
	time.sleep(0.01)
	print("waiting for the video")








# Example 1. Post A Comment
request_body = {
	'snippet': {
		'videoId': latestVideo,
		'topLevelComment': {
			'snippet': {
				'textOriginal': comment
			}
		}
	}
}

response = service.commentThreads().insert(
	part='snippet',
	body=request_body
).execute()

print(response)


# Example 2. Reply To A Comment
# comment_id = '<comment id>'
# request_body = {
# 	'snippet': {
# 		'parentId': comment_id,
# 		'textOriginal': 'Hello'
# 	}
# }

# response = service.comments().insert(
# 	part='snippet',
# 	body=request_body
# ).execute()