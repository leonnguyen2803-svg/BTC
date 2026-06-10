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

btc_buy_usd = 63200
btc_vnd_rate = 25000

btc_vnd = btc_usd * btc_vnd_rate

btc_invest_vnd = 100_000_000

btc_buy_vnd = btc_buy_usd * btc_vnd_rate

btc_value_now_vnd = (btc_invest_vnd / btc_buy_vnd) * btc_vnd

btc_profit_pct = ((btc_usd - btc_buy_usd) / btc_buy_usd) * 100
btc_profit_vnd = btc_value_now_vnd - btc_invest_vnd

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
                gold_price = int(price.replace(".", "").replace(",", ""))
                break
except:
    gold_price = None

gold_buy = 17_300_000 * 20

if gold_price:
    gold_profit_pct = ((gold_price - gold_buy) / gold_buy) * 100
    gold_profit_vnd = gold_price - gold_buy
else:
    gold_profit_pct = None
    gold_profit_vnd = None

# ================= OUTPUT =================
message = f"""BTC: {btc_usd:,.0f} USD
BTC: {btc_vnd:,.0f} VND
BTC P/L: {btc_profit_pct:+.2f}% ({btc_profit_vnd:+,.0f} VND)

Nhẫn vàng trơn 1 chỉ: {gold_price if gold_price else 'N/A'} VND
GOLD P/L: {gold_profit_pct:+.2f}% ({gold_profit_vnd:+,.0f} VND) 
"""

requests.post(
    WEBHOOK,
    json={"content": message}
)

print("DONE")
