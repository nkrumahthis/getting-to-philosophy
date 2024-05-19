import time
from flask import Flask, Response
import main

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to Getting-to-Philosophy</h1><a href='/stream/'>Stream</a>"

def scrape():
    hits = []
    link = "/wiki/Special:Random"

    while True:
        link = main.hit(link)
        yield("link " + link + "\n")

        if(link in hits):
            yield "Hit a loop! Already explored " + link + "\n"
            break

        hits.append(link)

        if(link == "/wiki/Philosophy"):
            yield "You have reached the Wikipedia page for Philosophy!\n"
            break

        yield "Following the first link: https://en.wikipedia.org" + link + "\n"


@app.route('/stream')
def stream():
    return Response(scrape(), mimetype="text/event-stream")