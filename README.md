# Getting to Philosophy

I read/heard somewhere years ago that if you click on the first link of any Wikipedia article long enough, you get to either the article on Mathematics or Philosophy.

I wrote this scraper to test that.

## Requirements

- Python 3+
- BeautifulSoup 4+
- requests

## Usage

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
./gtp
```

## Example

```
Exploring Wikipedia to reach Philosophy page...
Starting from a random Wikipedia article...

Exploring: André Green (psychoanalyst)
Following the first link: https://en.wikipedia.org/wiki/Cairo
Exploring: Cairo
Following the first link: https://en.wikipedia.org/wiki/Capital_city
Exploring: Capital city
Following the first link: https://en.wikipedia.org/wiki/Municipality
Exploring: Municipality
Following the first link: https://en.wikipedia.org/wiki/Administrative_division
Exploring: Administrative division
Following the first link: https://en.wikipedia.org/wiki/Sovereign_state
Exploring: Sovereign state
Following the first link: https://en.wikipedia.org/wiki/State_(polity)
Exploring: State (polity)
Following the first link: https://en.wikipedia.org/wiki/Politics
Exploring: Politics
Following the first link: https://en.wikipedia.org/wiki/Decision-making
Exploring: Decision
Following the first link: https://en.wikipedia.org/wiki/Psychology
Exploring: Psychology
Following the first link: https://en.wikipedia.org/wiki/Mind
Exploring: Mind
Following the first link: https://en.wikipedia.org/wiki/Thought
Exploring: Thought
Following the first link: https://en.wikipedia.org/wiki/Consciousness
Exploring: Consciousness
Following the first link: https://en.wikipedia.org/wiki/Awareness
Exploring: Awareness
Following the first link: https://en.wikipedia.org/wiki/Philosophy
You have reached the Wikipedia page for Philosophy!
```