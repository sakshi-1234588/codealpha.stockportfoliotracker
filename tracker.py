import csv

# Stock Portfolio Tracker
def stock_tracker():
    # Hardcoded dictionary of stock prices (USD per share)
    stock_prices = {
        "AAPL": 180,     # Apple
        "TSLA": 250,     # Tesla
        "GOOG": 135,     # Alphabet
        "AMZN": 140,     # Amazon
        "MSFT": 320      # Microsoft
    }

    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"   {stock} : ${price} per share")

    portfolio = {}

    # Take user input for stocks
    while True:
        stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("⚠️ Stock not found. Choose from the list above.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name} shares: "))
            if quantity <= 0:
                print("⚠️ Quantity must be positive.")
                continue
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    # Calculate total investment
    total_investment = 0
    print("\n💼 Your Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_investment += value
        print(f"   {stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

    print(f"\n Total Investment Value: ${total_investment}")

    # Save option
    save = input("\nDo you want to save this to a file? (y/n): ").lower()
    if save == "y":
        # 1️⃣ Save as text file
        filename_txt = "portfolio_summary.txt"
        with open(filename_txt, "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-----------------------\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(f"💾 Portfolio saved to {filename_txt}")

        # 2️⃣ Save as CSV file
        filename_csv = "portfolio_summary.csv"
        with open(filename_csv, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                total = qty * price
                writer.writerow([stock, qty, price, total])
            writer.writerow([])
            writer.writerow(["", "", "Total Investment", total_investment])
        print(f"💾 Portfolio also saved to {filename_csv}")

if __name__ == "__main__":
    stock_tracker()
