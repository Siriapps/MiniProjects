import json
from urllib import request
import os

tagsList = []
apiKey = os.getenv("YOUTUBE_APIKEY")
def getLatestVideos(channel_Id, maxVideos):
    part = "snippet"
    url = f"https://www.googleapis.com/youtube/v3/search?part={part}&channelId={channel_Id}&maxResults={maxVideos}&order=date&type=video&key={apiKey}"
    try:
        req = request.urlopen(url)
        data = req.read().decode()
        tags = json.loads(data)
        items = tags['items']
        for item in items:
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            videoId = item["id"]["videoId"]
            tagsList.append({
                "Title" : title,
                "Description":description,
                "Video ID":videoId,
                "Video Url":f"https://www.youtube.com/watch?v={videoId}"
            })

    except Exception as e:
        print("Error ",e)
    return tagsList


id = input("Enter Youtube channel Id: ")
MaxCount = input("Enter how many latest videos you want: ")
parse = getLatestVideos(id,MaxCount)
print(json.dumps(parse,indent=2))
