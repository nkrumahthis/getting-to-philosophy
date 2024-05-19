import main


def scrape(target):
    hits = []
    link = main.hit("/wiki/Special:Random")

    while True:
        link = main.hit(link)
        print(link)

        if(link in hits):
            print("Hit a loop! Already explored " + link)
            break

        hits.append(link)

        if(link == "/wiki/Philosophy"):
            print("You have reached the Wikipedia page for Philosophy!")
            break

        print("Following the first link: https://en.wikipedia.org" + link)