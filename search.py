import urllib3
import json

def search(search_keyword, API_KEY):
    url='https://www.googleapis.com/youtube/v3/search?type=channel&part=snippet&q='+search_keyword+'&key='+API_KEY
    http=urllib3.PoolManager()
    r=http.request('GET',url)
    json_data=json.loads(r.data.decode('utf-8'))
    try:
        response_results=json_data['items']
        for x in json_data['items']:
            print(x['snippet']['title'])
            print(x['snippet']['description'])
            print(x['id']['channelId'])
            print(x['snippet']['thumbnails']['high']['url'])
            print()
    except:
        print("Invalid request")
