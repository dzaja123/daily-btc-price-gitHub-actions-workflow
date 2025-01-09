import requests
from datetime import datetime


def fetch_btc_price() -> float:
    """
    Fetches the current Bitcoin price in USD from the CoinGecko API.

    Returns:
        float: The current price of Bitcoin in USD.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['bitcoin']['usd']


def update_readme(price: float) -> None:
    """
    Updates the README file with the latest Bitcoin price and the current date/time.

    Args:
        price (float): The latest Bitcoin price in USD to be displayed in the README.
    """
    # Get the current date and time
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    # Read the current README file
    with open("README.md", "r") as file:
        content = file.readlines()

    # Find the line where the Bitcoin price is updated or create a new one
    updated = False
    for idx, line in enumerate(content):
        if line.startswith("### Last updated Bitcoin price"):
            content[idx] = f"### 🚨 **Current Bitcoin Price**: **💰 ${price:,.2f} USD** 🤑\n_Last updated on {current_time}_\n"
            updated = True
            break
    
    # If not found, add a new section to the README
    if not updated:
        content.append(f"\n### 🚨 **Current Bitcoin Price**: **💰 ${price:,.2f} USD** 🤑\n_Last updated on {current_time}_\n")

    # Write the updated content back to README.md
    with open("README.md", "w") as file:
        file.writelines(content)


def main() -> None:
    """
    Main function to fetch the latest Bitcoin price and update the README file.
    """
    price = fetch_btc_price()
    update_readme(price)


if __name__ == "__main__":
    main()
