import requests
from bs4 import BeautifulSoup

TOP_URL = "https://rugby.statbunker.com/competitions/"

def get_comp_urls():
    page = requests.get(TOP_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    links = soup.find_all("a", {"class": "pointer"})

    urls = list(map(lambda x: x.get("href"), links))

    return urls

def get_wc_data(comp_id):
    URL = f"https://rugby.statbunker.com/competitions/Sections?comp_id={comp_id}"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    ## The links are in a table with class "breadcrumb"
    section_ids = [li.a.get("href")[-3:]
                     for li in soup.find("ul", {"class", "breadcrumb"}).find_all("li")]

    ## -- Pool Section -- ##

    page = requests.get(f"https://rugby.statbunker.com/competitions/Sections?comp_id={comp_id}&section_id={section_ids[0]}")
    pool_top_soup = BeautifulSoup(page.content, "html.parser")

    group_ids = [tr.td.a.get("href")[-3:]
                 for tr in pool_top_soup.find_all("tr", {"class": "genericFooter"})]
    
    ## Loop over the the pool groups
    for group_id in group_ids:
        ## Link for base page for a given group
        group_link = f"https://rugby.statbunker.com/competitions/Sections?comp_id={comp_id}&section_id={section_ids[0]}&group_id={group_id}"

        page = requests.get(group_link)
        group_soup = BeautifulSoup(page.content, "html.parser")

        ## Filter all the links from the base group page using the match detail stem
        filter_func = lambda x: x.startswith("https://rugby.statbunker.com/competitions/MatchDetails/")
        game_links = list(set(filter(filter_func, (a.get("href") for a in group_soup.find_all("a")))))


if __name__ == "__main__":
    get_wc_data(606)