import requests
import os
from bs4 import BeautifulSoup

WEBHOOK = os.environ["DISCORD_WEBHOOK"]
headers = {"User-Agent": "Mozilla/5.0"}

# ================= BTC =================
btc_usd = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
    timeout=10
).json()["bitcoin"]["usd"]

btc_vnd = btc_usd * 25000

# ================= GOLD =================
try:
    url = "https://ngoctham.com/bang-gia-vang/"
    res = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")

    gold_price = None

    for row in soup.select("table tr"):
        cols = row.find_all("td")
        if len(cols) >= 3:
            name = cols[0].get_text(strip=True)
            price = cols[2].get_text(strip=True)

            if "Nhẫn 999.9" in name:
                gold_price = price
                break
except:
    gold_price = None

# ================= DISCORD =================
message = f"""📊 MARKET REPORT

BTC: ${btc_usd:,.0f}
BTC: {btc_vnd:,.0f} VND
Nhẫn vàng trơn 1 chỉ: {gold_price or 'N/A'} VND
"""

requests.post(
    WEBHOOK,
    json={"content": message}
)

print("DONE")
