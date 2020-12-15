from flask import Flask, render_template
from datetime import date, timedelta

app=Flask(__name__)

from videos import videos
from read import read
from credentials import connection_url
from credentials import API_KEY
from actions import find, insert

@app.route("/")
def index():
    today=(date.today()).strftime("%Y-%m-%d")
    result=find('Date',today)
    if(result is None):
        print('Need to invoke API')
        list_of_id=read()
        titles, description, video_id, thumbnails, published_at, url=videos(list_of_id, API_KEY)
        insert(today, titles, description, video_id, thumbnails, published_at, url)
        return render_template("index.html",n=len(titles), titles=titles, description=description, video_id=video_id, thumbnails=thumbnails, published_at=published_at, url=url)
    else:
        print('Data already present')
        return render_template("index.html",n=len(result['Title']), titles=result['Title'], description=result['Desc'], video_id=result['V_ID'], thumbnails=result['Thumb'], published_at=result['Pub'], url=result['URL'])

if __name__=="__main__":
    app.run(debug=True)