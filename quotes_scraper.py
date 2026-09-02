import requests
from bs4 import BeautifulSoup
import json
import asyncio
import aiohttp
import time

time1 = time.time()
url_list = []

def next_url(soup):
    next_link = soup.select_one("li.next a")
    if next_link:
        link = next_link.get("href")
        return f"https://quotes.toscrape.com{link}"
    return None

current_url = "https://quotes.toscrape.com/"

# Phase 1: Making URL list
while current_url:
    r = requests.get(current_url)
    soup = BeautifulSoup(r.content, "html.parser")
    url_list.append(current_url)
    current_url = next_url(soup)
print("URLs completed!")    
    
# Phase 2: Async fetch
async def fetch(url, session):
    headers = {"User-agent": "SmartScraper/1.0"}
    async with session.get(url, headers=headers) as response:
        return await response.text()
        
async def doing_task():
    task = []        
    async with aiohttp.ClientSession() as session:
        for i in url_list:
            task.append(fetch(i, session))
        results = asyncio.gather(*task)
        return await results

list_of_dict = []   

def parse_data(results):
    for html_page in results:
        soup = BeautifulSoup(html_page, "html.parser")
        for i in soup.select(".quote"):
            # Safe parsing without zip
            quote = i.select_one(".text")
            author = i.select_one(".author")
            tags = i.select_one(".tags")
            
            book_dict = {
                "Quote": quote.text if quote else "N/A", 
                "Author": author.text if author else "N/A", 
                "Tags": tags.text.strip().replace("\n", " ") if tags else "N/A"
            }
            list_of_dict.append(book_dict)
    
results = asyncio.run(doing_task())
parse_data(results)
print("Parsing completed....")

count = 0
for i in list_of_dict:
    for key, value in i.items():
        print(f"{key} -> {value}")
    count += 1
print(f"Total Quotes Scraped: {count}")
print(f"Asyncio total time -> {time.time() - time1} sec")

# Saving data to JSON file automatically
with open("quotes_data.json", "w") as f:
    json.dump(list_of_dict, f, indent=4)
