from flask import Flask, render_template

app=Flask(__name__)

from videos import videos
from read import read

@app.route("/")
def index():
    
    list_of_id=read()
    titles, description, video_id, thumbnails, published_at, url=videos(list_of_id, API_KEY)
    '''
    print(titles)
    print(description)
    print(video_id)
    print(thumbnails)
    print(published_at)
    '''
    return render_template("index.html",n=len(titles), titles=titles, description=description, video_id=video_id, thumbnails=thumbnails, published_at=published_at, url=url)

if __name__=="__main__":
    app.run(debug=True)