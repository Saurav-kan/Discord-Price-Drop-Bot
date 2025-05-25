import aiohttp
from bs4 import BeautifulSoup
from config import HEADERS

async def fetch_price(session: aiohttp.ClientSession, url: str) -> float:
   
   # Scrapes amazon product page for its price.
    async with session.get(url, headers=HEADERS) as resp:
        text = await resp.text()
    soup = BeautifulSoup(text, "html.parser")

    price_str = (
        soup.select_one("#priceblock_ourprice") or
        soup.select_one("#priceblock_dealprice")
    )
    if not price_str:
        raise ValueError("Could not find price on page")
    # e.g. "$1,234.56" → "1234.56"
    return float(price_str.text.strip().replace("$", "").replace(",", ""))
