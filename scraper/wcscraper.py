import requests
from bs4 import BeautifulSoup
import tqdm

TOP_URL = "https://rugby.statbunker.com/competitions/"

stats_page_filter_func = lambda x: x.startswith("https://rugby.statbunker.com/competitions/MatchDetails/")

def get_wc_data(comp_id):
    links = get_wc_game_links(comp_id)
    

def get_wc_game_links(comp_id):
    URL = f"{TOP_URL}Sections?comp_id={comp_id}"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    ## The links are in a table with class "breadcrumb"
    section_ids = [li.a.get("href")[-3:] for li in soup.find("ul", {"class", "breadcrumb"}).find_all("li")]

    game_links = get_pool_game_links(comp_id, section_ids[0])
    game_links += get_non_pool_game_links(comp_id, section_ids[1:])

    return game_links

def get_pool_game_links(comp_id, section_id):
    page = requests.get(f"{TOP_URL}Sections?comp_id={comp_id}&section_id={section_id}")
    soup = BeautifulSoup(page.content, "html.parser")

    group_ids = [tr.td.a.get("href")[-3:]
                 for tr in soup.find_all("tr", {"class": "genericFooter"})]
    
    pool_game_links = []
    
    ## Loop over the the pool groups
    for group_id in group_ids:
        ## Link for base page for a given group
        group_link = f"{TOP_URL}Sections?comp_id={comp_id}&section_id={section_id}&group_id={group_id}"

        page = requests.get(group_link)
        group_soup = BeautifulSoup(page.content, "html.parser")

        ## Filter all the links from the base group page using the match detail stem
        pool_game_links += list(set(filter(stats_page_filter_func, (a.get("href") for a in group_soup.find_all("a")))))

    return pool_game_links

def get_non_pool_game_links(comp_id, section_ids):
    non_pool_game_links = []

    ## Seeing as there aren't any sublinks in the non pool games then the search for game stat links can be done
    ## directly
    for section_id in section_ids:
        page = requests.get(f"{TOP_URL}Sections?comp_id={comp_id}&section_id={section_id}")
        non_pool_soup = BeautifulSoup(page.content, "html.parser")
        non_pool_game_links += list(set(filter(stats_page_filter_func, (a.get("href") for a in non_pool_soup.find_all("a")))))

    return non_pool_game_links