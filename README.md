# Stock Portfolio Tracker

## About the Project

The Stock Portfolio Tracker is a beginner-friendly Python application that allows users to record stock holdings and calculate the total value of their portfolio using predefined stock prices.

The program displays a list of available stock symbols and their prices. Users can select stocks, enter the number of shares they own, and view a portfolio summary showing each stock's quantity, price per share, and total holding value.

The application also allows users to save their portfolio report as a CSV or TXT file for future reference.

## Features

- Displays five predefined stock symbols and their prices.
- Allows users to select stocks and enter share quantities.
- Updates quantities when the same stock is entered more than once.
- Validates stock symbols and handles invalid quantity inputs.
- Calculates the value of individual stock holdings.
- Calculates the total portfolio value.
- Generates a portfolio summary.
- Exports reports to CSV or TXT files.

## Technologies Used

- **Python:** Core programming language.
- **CSV module:** Writes portfolio reports in CSV format.
- **Dictionaries:** Stores stock prices and portfolio quantities.
- **Functions:** Organises the program into a reusable function.
- **Exception handling:** Handles invalid numeric input and file-saving errors.
- **File handling:** Creates and saves portfolio reports.

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in your code editor or terminal.
4. Run the following command:

```bash
python stock_portfolio_tracker.py
```

Replace `stock_portfolio_tracker.py` with your actual Python filename if it differs.

## How to Use the Application

1. Run the program.
2. Review the available stock symbols and their predefined prices.
3. Enter a stock symbol, such as AAPL or TSLA.
4. Enter the quantity of shares.
5. Repeat to add more stocks.
6. Type `done` to finish entering holdings.
7. Review the portfolio summary and total investment value.
8. Choose whether to save the report as a CSV file, a TXT file, or not at all.

## Learning Objectives

This project provided practical experience with Python dictionaries, loops, conditional statements, functions, user input, input validation, exception handling, calculations, and file operations.

It also helped me understand how different Python concepts can work together to build a useful command-line application.

## Limitations

The stock prices are predefined sample values and are not updated using live market data. The calculated portfolio value is therefore an estimate based on the values supplied in the program, not a real-time valuation or investment recommendation.

## Future Improvements

- Retrieve live stock prices through a reliable financial API.
- Allow users to add new stock symbols and prices.
- Store portfolio data between sessions.
- Add a graphical user interface.
- Include purchase prices and profit-or-loss calculations.
