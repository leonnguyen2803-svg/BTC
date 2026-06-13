# ================= OUTPUT =================
message = f"""BTC: {btc_usd:,.0f} USD
BTC: {btc_vnd:,.0f} VND
Lợi nhuận: {btc_profit_pct:+.2f}% ({btc_profit_vnd:+,.0f} VND)

Nhẫn vàng trơn 1 chỉ: {gold_price if gold_price else 'N/A'} VND
Lợi nhuận: {gold_profit_pct:+.2f}% ({gold_profit_vnd:+,.0f} VND)

Thông tin hiện tại: {total_profit_pct:+.2f}% ({total_profit_vnd:+,.0f} VND)

Tổng tài sản: {total_now:,.0f} VND
"""

requests.post(
    WEBHOOK,
    json={"content": message}
)

print("DONE")
