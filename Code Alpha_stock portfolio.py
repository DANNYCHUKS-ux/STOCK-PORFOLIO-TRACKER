import csv


def stock_portfolio_tracker():
    # Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 410,
        "AMZN": 175
    }

    portfolio = {}
    total_investment = 0.0

    print("=== Welcome to the Stock Portfolio Tracker ===")
    print("Available stocks and their current prices:")
    for stock, price in stock_prices.items():
        print(f"  - {stock}: ${price}")
    print("-" * 45)

    # User inputs stock names and quantity
    while True:
        stock_name = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()

        if stock_name == 'DONE':
            break

        if stock_name not in stock_prices:
            print(f"Error: '{stock_name}' is not in the price list. Please choose from: {list(stock_prices.keys())}")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid whole number for quantity.")
            continue

        # Add to portfolio or update quantity if already entered
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name}.\n")

    if not portfolio:
        print("\nNo stocks were added to the portfolio.")
        return

    # Calculate total investment value
    print("\n" + "=" * 30)
    print("PORTFOLIO SUMMARY")
    print("=" * 30)

    summary_data = []
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        holding_value = price * qty
        total_investment += holding_value
        print(f"Stock: {stock} | Quantity: {qty} | Price: ${price} | Total: ${holding_value:.2f}")
        summary_data.append({"Stock": stock, "Quantity": qty, "Price": price, "Total Value": holding_value})

    print("-" * 30)
    print(f"Total Investment Value: ${total_investment:.2f}")
    print("=" * 30)

    # Optional: Save the result to a .csv or .txt file
    save_choice = input("\nWould you like to save this report to a file? (txt/csv/no): ").strip().lower()

    if save_choice == 'csv':
        filename = "portfolio_report.csv"
        try:
            with open(filename, mode='w', newline='') as csv_file:
                fieldnames = ["Stock", "Quantity", "Price", "Total Value"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in summary_data:
                    writer.writerow(row)
                csv_file.write(f"\nTotal Investment,,,{total_investment:.2f}")
            print(f"Successfully saved portfolio to {filename}!")
        except Exception as e:
            print(f"An error occurred while saving the CSV file: {e}")

    elif save_choice == 'txt':
        filename = "portfolio_report.txt"
        try:
            with open(filename, mode='w') as txt_file:
                txt_file.write("=== Stock Portfolio Report ===\n")
                for row in summary_data:
                    txt_file.write(
                        f"Stock: {row['Stock']}, Quantity: {row['Quantity']}, Price: ${row['Price']}, Total: ${row['Total Value']:.2f}\n")
                txt_file.write(f"\nTotal Investment Value: ${total_investment:.2f}\n")
            print(f"Successfully saved portfolio to {filename}!")
        except Exception as e:
            print(f"An error occurred while saving the TXT file: {e}")

    else:
        print("Report not saved to file. Thank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    stock_portfolio_tracker()