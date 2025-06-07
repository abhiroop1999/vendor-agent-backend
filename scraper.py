import requests
from bs4 import BeautifulSoup

def scrape_alibaba(product_name):
    search_url = f"https://www.alibaba.com/trade/search?SearchText={product_name}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    vendors = []
    for card in soup.select(".J-offer-wrapper")[:5]:
        name = card.select_one(".elements-title-normal__outter").text.strip() if card.select_one(".elements-title-normal__outter") else "Unknown"
        price = card.select_one(".elements-offer-price-normal__price").text.strip() if card.select_one(".elements-offer-price-normal__price") else "N/A"
        vendors.append({"name": name, "price": price})

    return vendors