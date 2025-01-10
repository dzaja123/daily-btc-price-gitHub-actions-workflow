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

    # Update or replace the Bitcoin price and timestamp
    updated_content = []
    updated = False
    for line in content:
        if line.startswith("### 🚨 **Current Bitcoin Price"):
            updated_content.append(f"### 🚨 **Current Bitcoin Price**: **💰 ${price:,.2f} USD** 💰\n")
            updated = True
        elif line.startswith("_Last updated on"):
            if updated:
                updated_content.append(f"_Last updated on {current_time}_\n")
                updated = False  # Reset the flag
        else:
            updated_content.append(line)

    # Ensure timestamp is added if not already present
    if updated:
        updated_content.append(f"_Last updated on {current_time}_\n")

    # Write the updated content back to README.md
    with open("README.md", "w") as file:
        file.writelines(updated_content)

def main() -> None:
    """
    Main function to fetch the latest Bitcoin price and update the README file.
    """
    price = fetch_btc_price()
    update_readme(price)


if __name__ == "__main__":
    main()
