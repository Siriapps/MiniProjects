import json
from urllib import request
import os

tagsList = []
apiKey = os.getenv("YOUTUBE_APIKEY")

def readVideoLink(videoId):
    part = "snippet"
    url = f"https://youtube.googleapis.com/youtube/v3/videos?part={part}&id={videoId}&key={apiKey}"
    try:
        req = request.urlopen(url)
        data = req.read().decode()
        tags = json.loads(data)
        items = tags['items']
        for item in items:
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            tagsList.append({
                "Title" : title,
                "Description":description
            })
    except Exception as e:
        print("Error ",e)
    return tagsList

id = input("Enter your Youtube video Id: ")
parse = readVideoLink(id)
print(json.dumps(parse,indent=2))