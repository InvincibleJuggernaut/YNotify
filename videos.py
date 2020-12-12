import urllib3
import json
from datetime import date, timedelta

def videos(channel_id, API_KEY):
    url='https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&channelId='+channel_id+'&part=snippet,id&order=date&maxResults=5'
    http=urllib3.PoolManager()
    r=http.request('GET',url)
    json_response=json.loads(r.data.decode('utf-8'))
    list_of_days=[]
    today=date.today()
    today_date_ordered=today.strftime("%Y-%m-%d")
    for i in range(0,7):
        day=today-timedelta(days=i)
        day_ordered=day.strftime("%Y-%m-%d")
        list_of_days.append(day_ordered)
    try:
        response_results=json_response['items']
        for x in response_results:
            published_details=x['snippet']['publishedAt']
            published_date=published_details[0:10]
            if(published_date in list_of_days):
                print(x['snippet']['title'])
                print(x['snippet']['description'])
                print(x['id']['videoId'])
                print(x['snippet']['thumbnails']['default']['url'])
                print(x['snippet']['publishedAt'])
            
    except:
        print('Invalid request')
    


