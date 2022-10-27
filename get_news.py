"""
Tools to scrape web for articles related to different themes
"""
import requests
import re
from bs4 import BeautifulSoup

# Define news website
URL = "https://www.reuters.com/"

# Keywords for theme
KEYWORDS = {
  "climate_change": ["environment", "greenhouse", "climate"],
  "famine": ["famine", "hunger", "starve", "starving"],
  "nuclear_war": ["nuclear", "war", "radioactive", "russia", "ukraine", "north korea"],
  "pandemic": ["covid", "pandemic", "flu", "pox", "infection"],
  "machine_superintelligence": ["ai", "artificial intelligence", "robot", "superintelligen"],
  "crop_failure": ["crop failure"],
}

# Function to make request to site 
def get_article(theme):
  # Get keywords associated with theme
  theme_keywords = KEYWORDS[theme]
  # Make request to URL
  page = requests.get(URL)
  # Parse the html response with BeautifulSoup
  soup = BeautifulSoup(page.content, "html.parser")
  # Get story headings
  headings = soup.find_all("a", attrs={"data-testid": "Heading"})

  #Set default output data
  story_text = "no stories available"
  story_URL = "no story URL"

  # Loop through all headings, and see if any headings contain the keywords
  # Get the text and link to the story for the first match
  for h in headings:
    if any(word.upper() in h.text.upper() for word in theme_keywords):
      story_text = h.text
      story_URL = h["href"]
      break

  # Dictionary for output data
  article_info = {
    "text": story_text, 
    "url": story_URL
    }

  return article_info
