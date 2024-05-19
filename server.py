import json
import time
from flask import Flask, Response
import main

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to Getting-to-Philosophy</h1><a href='/stream/'>Stream</a>"

def crawl():
    hits = []
    link = "/wiki/Special:Random"

    while True:
        link = main.hit(link)

        if(link in hits):
            print("Hit a loop! Already explored " + link)
            break

        hits.append(link)

        print("link " + link + "\n")
        yield json.dumps({
            'previous': hits[-1],
            'next': link
        })

        if(link == "/wiki/Philosophy"):
            print( "You have reached the Wikipedia page for Philosophy!")
            break

        print( "Following the first link: https://en.wikipedia.org" + link)


@app.route('/stream')
def stream():
    return Response(crawl(), mimetype="text/event-stream")