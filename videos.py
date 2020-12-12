import urllib3
import json

def videos(channel_id, API_KEY):
    url='https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&channelId='+channel_id+'&part=snippet,id&order=date&maxResults=10'
    http=urllib3.PoolManager()
    r=http.request('GET',url)
    json_response=json.loads(r.data.decode('utf-8'))
    try:
        response_results=json_response['items']
        for x in response_results:
            print(x['snippet']['title'])
            print(x['snippet']['description'])
            print(x['id']['videoId'])
            print(x['snippet']['thumbnails']['default']['url'])
            print()
    except:
        print('Invalid request')
