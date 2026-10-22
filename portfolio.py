import csv
from datetime import datetime

# Stock Portfolio Performance Tracker
# Enter the latest market price manually; this version does not fetch live prices.

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number, for example 125.50.")


def main():
    print("=" * 52)
    print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 52)
    print("Enter ticker, buy price, share quantity, and latest market price.")
    print("Note: You must enter the latest market price yourself.\n")

    portfolio = []
    while True:
        ticker = input("Stock ticker symbol (e.g. AAPL): ").strip().upper()
        if not ticker:
            print("Ticker symbol cannot be empty.")
            continue

        buy_price = get_positive_number("Buy price per share: ")
        quantity = get_positive_number("Number of shares: ")
        current_price = get_positive_number("Latest market price per share: ")

        invested = buy_price * quantity
        market_value = current_price * quantity
        gain_loss = market_value - invested
        gain_loss_percent = (gain_loss / invested) * 100

        portfolio.append({
            "ticker": ticker,
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price,
            "invested": invested,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "gain_loss_percent": gain_loss_percent,
        })

        more = input("Add another stock? (y/n): ").strip().lower()
        if more != "y":
            break
        print()

    total_invested = sum(item["invested"] for item in portfolio)
    total_market_value = sum(item["market_value"] for item in portfolio)
    total_gain_loss = total_market_value - total_invested
    total_gain_loss_percent = (total_gain_loss / total_invested) * 100 if total_invested else 0

    print("\n" + "=" * 86)
    print("PORTFOLIO SUMMARY")
    print("=" * 86)
    print(f"{'Ticker':<10}{'Buy Price':>12}{'Shares':>10}{'Market Price':>15}{'Invested':>14}{'Market Value':>15}{'Gain/Loss %':>13}")
    print("-" * 86)
    for item in portfolio:
        print(
            f"{item['ticker']:<10}{item['buy_price']:>12.2f}{item['quantity']:>10g}"
            f"{item['current_price']:>15.2f}{item['invested']:>14.2f}"
            f"{item['market_value']:>15.2f}{item['gain_loss_percent']:>12.2f}%"
        )
    print("-" * 86)
    print(f"Total invested:       {total_invested:.2f}")
    print(f"Current market value: {total_market_value:.2f}")
    print(f"Total gain/loss:      {total_gain_loss:.2f} ({total_gain_loss_percent:.2f}%)")

    filename = "portfolio_summary.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["timestamp", "ticker", "buy_price", "quantity", "current_price",
                      "invested", "market_value", "gain_loss", "gain_loss_percent"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in portfolio:
            row = {"timestamp": timestamp}
            row.update(item)
            writer.writerow(row)
        writer.writerow({
            "timestamp": timestamp, "ticker": "TOTAL", "buy_price": "",
            "quantity": "", "current_price": "", "invested": round(total_invested, 2),
            "market_value": round(total_market_value, 2), "gain_loss": round(total_gain_loss, 2),
            "gain_loss_percent": round(total_gain_loss_percent, 2)
        })

    print(f"\nPortfolio results saved to '{filename}'.")
    print("Reminder: this is a learning tool, not financial advice.")


if __name__ == "__main__":
    main()
