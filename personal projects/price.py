import http.client
import json
import urllib.parse


def get_card_price(card_name):
    # URL encode the card name to handle spaces and special characters
    encoded_card_name = urllib.parse.quote(card_name)

    # Create a connection to the Scryfall API
    conn = http.client.HTTPSConnection("api.scryfall.com")

    # Prepare the API request URL
    url = f"/cards/named?exact={encoded_card_name}"

    # Define headers (including User-Agent and Accept)
    headers = {
        "User-Agent": "Price/1.0",
        "Accept": "application/json",  # We're expecting JSON data in return
    }

    # Print the URL to verify it's correctly formatted
    print(f"Request URL: {url}")

    # Send the GET request to the API with the headers
    conn.request("GET", url, headers=headers)

    # Get the response from the server
    response = conn.getresponse()

    # Check the response status code
    if response.status == 200:
        data = response.read()
        card_data = json.loads(data)  # Parse the JSON response

        # Extract the price data from the JSON response
        prices = card_data.get("prices", {})

        if prices:
            # Get the USD price (or any other price you prefer)
            usd_price = prices.get("usd", "Price not available")
            return usd_price
        else:
            return "No price data found"
    else:
        # Break the error message into multiple lines to avoid exceeding the maximum len
        error_message = response.read().decode("utf-8")
        return (
            f"Error: Unable to fetch data (status code {response.status}). "
            f"Message: {error_message}"
        )


# Example usage
card_name = "The One Ring"  # Replace with your desired card name
price = get_card_price(card_name)
print(f"The price of {card_name} is: {price}")


def get_multiple_prices(card_names: list[str]) -> dict[str, float]:
    prices = {}
    for card_name in card_names:
        price = get_card_price(card_name)
        prices[card_name] = price

    total: float = 0.0
    for key in prices:
        total += prices[key]

    print(total)
    return prices
