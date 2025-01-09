import requests
from datetime import datetime


# Fetch Bitcoin price from CoinGecko API
def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

# Update README file
def update_readme(price):
    # Get the current date and time
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    # Read the current README file
    with open("README.md", "r") as file:
        content = file.readlines()

    # Find the line where the Bitcoin price is updated or create a new one
    updated = False
    for idx, line in enumerate(content):
        if line.startswith("### Last updated Bitcoin price"):
            content[idx] = f"### Last updated Bitcoin price: ${price} USD on {current_time}\n"
            updated = True
            break
    
    # If not found, add a new section to the README
    if not updated:
        content.append(f"\n### Last updated Bitcoin price: ${price} USD on {current_time}\n")

    # Write the updated content back to README.md
    with open("README.md", "w") as file:
        file.writelines(content)

# Main function to fetch price and update README
def main():
    price = fetch_btc_price()
    update_readme(price)


if __name__ == "__main__":
    main()
