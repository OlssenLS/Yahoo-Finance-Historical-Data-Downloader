import yfinance as yf

# To download historical data of stocks in Indonesia, use .JK at the end of the ticker. Example: BBCA.JK

# Download JKSE (IHSG) stock price history data from Jan 01, 2005 to Mar 27, 2025
data = yf.download("^JKSE", start="2005-01-01", end="2025-03-28", auto_adjust=False)
print("Downloaded data:")
print(data.head())  # Display the first few rows of the data
# Save the data to a CSV file
data.to_csv("IHSG_stock_data.csv")
print(f"Data saved to IHSG_stock_data.csv")