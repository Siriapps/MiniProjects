from dotenv import load_dotenv, set_key,find_dotenv

load_dotenv(find_dotenv())
import json
from urllib import request
import os

tagsList = []
apiKey = os.getenv("YOUTUBE_APIKEY")

def getLatestVideos(channel_Id, maxVideos):
    part = "snippet"
    type = "video"
    url = f"https://www.googleapis.com/youtube/v3/search?part={part}&channelId={channel_Id}&maxResults={maxVideos}&order=date&type={type}&key={apiKey}"
    etag = os.getenv("ETAG")
    try:
        hdr={
            'User-Agent' : 'PostmanRuntime/7.26.8',
            'If-None-Match': etag
        }
        req = request.Request(url,headers=hdr)
        response = request.urlopen(req)
        data = response.read().decode()
        tags = json.loads(data)

        items = tags['items']
        os.environ['ETAG']=tags['etag']
        set_key(find_dotenv(), "ETAG", os.environ["ETAG"])

        for item in items:
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            videoId = item["id"]["videoId"]
            tagsList.append({
                "Title" : title,
                "Description":description,
                "Video ID":videoId,
                "Video Url":f"https://www.youtube.com/watch?v={videoId}",
            })

    except Exception as e:
        print("Error ",e)
    return tagsList


id = input("Enter Youtube channel Id: ")
MaxCount = input("Enter how many latest videos you want: ")
parse = getLatestVideos(id,MaxCount)
print(json.dumps(parse,indent=2))

