import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_headlines.csv"

def scrape_hackernews():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    # Each headline is inside: span.titleline > a
    for idx, span in enumerate(soup.find_all("span", class_="titleline"), start=1):
        a_tag = span.find("a")
        if a_tag:
            title = a_tag.get_text(strip=True)
            link = a_tag["href"]
            headlines.append([idx, title, link])

    # Save to CSV
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["S.No", "Title", "Link"])
        writer.writerows(headlines)

    print(f"✅ Scraped {len(headlines)} Hacker News headlines")

if __name__ == "__main__":
    scrape_hackernews()
