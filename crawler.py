
import main
import json

def crawl():
    hits = []
    link = "/wiki/Special:Random"

    while True:
        link = main.hit(link)

        if(link in hits):
            print("Hit a loop! Already explored " + link)
            yield json.dumps({
                'previous': hits[-2] if len(hits) > 1 else hits[-1],
                'current': link
            })
            break

        hits.append(link)

        print("link " + link + "\n")
        yield json.dumps({
            'previous': hits[-2] if len(hits) > 1 else "/wiki/Special:Random",
            'current': link
        })

        if(link == "/wiki/Philosophy"):
            print( "You have reached the Wikipedia page for Philosophy!")
            break

        print( "Following the first link: https://en.wikipedia.org" + link)

