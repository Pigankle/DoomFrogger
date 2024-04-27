"""
Tools to search the web for articles related to different themes
"""
import requests
import re
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from collections import deque
from configuration.constants import KEYWORDS, NUM_ARTICLES, SEARCH_URL

# Dictionary to save all the news stories for a given search path
parsed_articles = {
    "climate_change": None,
    "famine": None,
    "nuclear_war": None,
    "pandemic": None,
    "machine_superintelligence": None,
    "crop_failure": None,
}


# Create data class for storing type of threat and article headline text
@dataclass
class ThreatHeadlines:
    threat: str = "climate_change"
    headlines: deque = field(default_factory=deque)

    # Override default __eq__ method for easier comparisons
    def __eq__(self, other):
        if other == self.threat:
            return True
        return False


# Function to make request to a news site at the path related to a given theme,
# and save the parsed html reponse
# Note: Should only need to do this once per day
def request_articles(theme):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        theme_path = KEYWORDS[theme]["path"]
        print(f"{theme_path=}")
        page = requests.get(f"{SEARCH_URL}{theme_path}", headers=headers)
        page.raise_for_status()  # Raises an exception for HTTP codes 400 and above
        soup = BeautifulSoup(page.content, "html.parser")
        articles = soup.find_all("span", class_="PagePromoContentIcons-text")
        print(f"{articles=}")
        return articles
    except requests.RequestException as e:
        print(f"Failed to fetch articles for theme {theme}: {e}")
        return []




# Function to request all stories for all themes
# and save the parsed headings in the saved_articles dictionary
def request_all_articles():
    # Get articles for each keyword
    for theme in KEYWORDS:
        # print(f"Loading articles for theme {theme}...\n")
        parsed_articles[theme] = request_articles(theme)


def insert_newlines(text, word_limit=10):
    words = text.split()
    # Insert a newline character after every `word_limit` words
    for i in range(word_limit, len(words), word_limit):
        words[i] = '\n   ' + words[i]
    return ' '.join(words)

def find_thematic_article(theme, num_articles, stored_headlines=None):
    if stored_headlines is None:
        stored_headlines = deque()
    article_counter = 1
    for idx, h in enumerate(parsed_articles[theme]):
        if article_counter > num_articles:
            break
        if any(word.upper() in h.text.upper() for word in KEYWORDS[theme]["keywords"]):
            formatted_headline = insert_newlines(h.text)  # Format the headline to insert newlines
            print(f"Loading article #{article_counter}...\n")
            stored_headlines.append(formatted_headline)
            parsed_articles[theme].pop(idx)  # Remove the article to avoid duplicates
            article_counter += 1
    return stored_headlines



# Function to get thematicx articles for all keywords and save them for use in the game
# E.G. at game start you would run request_all_articles() and then stock_all_articles(3) to get
# 3 articles for each theme
def stock_all_articles(num_articles):
    # List for storing articles
    saved_headlines = []

    # Get articles for each keyword
    for theme in KEYWORDS:
        print(f"\nLoading articles for theme {theme}...\n")
        # Get an article related to a theme, store the theme and article headline in a
        # threat_headline object, and append the stored object to the list of saved objects
        saved_headlines.append(
            ThreatHeadlines(theme, find_thematic_article(theme=theme, num_articles=num_articles))
        )

    return saved_headlines


# Function to return a saved article or get new articles if there are none left
def replenish_articles(threat, stored_articles):
    for article in stored_articles:
        # Find an article related to a given threat
        if article == threat:
            # If there are no articles left, get more articles
            if not article.headlines:
                print("Need to replenish supply of articles!\n")
                find_thematic_article(
                    theme=threat,
                    num_articles=NUM_ARTICLES,
                    # Pass in the existing headlines object
                    # so we can append articles directly to that object
                    stored_headlines=article.headlines,
                )

            # Return an article and remove it from our collection of stored articles
            try:
                return article.headlines.pop()
            except:
                return f"Overwhelming {threat}"


# TODO: Add sentiment analysis for article headlines to get only negative headlines?

# Example usage:
# Request article text and stored parsed html
# request_all_articles()
# Find thematic articles from parsed html and save in list
# saved_articles = stock_all_articles(num_articles = NUM_ARTICLES)
# Replenish articles
# replenish_articles("crop_failure", saved_articles)
