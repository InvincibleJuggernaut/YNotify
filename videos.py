import urllib3
import json
from datetime import date, timedelta

def videos(list_of_id, API_KEY):
    list_of_days=[]
    list_of_titles=[]
    list_of_description=[]
    list_of_video_id=[]
    list_of_thumbnails=[]
    list_of_published_at=[]
    list_of_url=[]

    today=date.today()
    today_date_ordered=today.strftime("%Y-%m-%d")
    for i in range(0,7):
        day=today-timedelta(days=i)
        day_ordered=day.strftime("%Y-%m-%d")
        list_of_days.append(day_ordered)
    
    for channel_id in list_of_id:
        url='https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&channelId='+channel_id+'&part=snippet,id&order=date&maxResults=5'
        http=urllib3.PoolManager()
        r=http.request('GET',url)
        json_response=json.loads(r.data.decode('utf-8'))    
        try:
            response_results=json_response['items']
            for x in response_results:
                published_details=x['snippet']['publishedAt']
                published_date=published_details[0:10]
                if(published_date in list_of_days):
                    list_of_titles.append(x['snippet']['title'])
                    list_of_description.append(x['snippet']['description'])
                    list_of_video_id.append(x['id']['videoId'])
                    list_of_thumbnails.append(x['snippet']['thumbnails']['high']['url'])
                    list_of_published_at.append(x['snippet']['publishedAt'])
                    list_of_url.append('https://www.youtube.com/watch?v='+x['id']['videoId'])
                
                '''
                print(x['snippet']['title'])
                print(x['snippet']['description'])
                print(x['id']['videoId'])
                print(x['snippet']['thumbnails']['high']['url'])
                print(x['snippet']['publishedAt'])
                '''    
        except:
            print('Quota exceeded')
    return list_of_titles, list_of_description, list_of_video_id, list_of_thumbnails, list_of_published_at, list_of_url
    


