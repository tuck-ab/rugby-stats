import requests
from bs4 import BeautifulSoup

from wcscraper import get_wc_data
from matchscraper import get_match_data

TOP_URL = "https://rugby.statbunker.com/competitions/"

def get_comp_urls():
    page = requests.get(TOP_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    links = soup.find_all("a", {"class": "pointer"})

    urls = list(map(lambda x: x.get("href"), links))

    return urls




if __name__ == "__main__":
    get_match_data("https://rugby.statbunker.com/competitions/MatchDetails/World-Cup-2019/England-VS-South-Africa?comp_id=606&match_id=40373&date=02-Nov-2019")