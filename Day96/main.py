import requests
import json
import time
from datetime import datetime
from random import randint

product_name = "RTX 3080 FE"
URL = "https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&locations=938%7C202%7C617%7C203%7C57%7C926%7C977%7C233%7C930%7C927%7C62%7C622%7C931%7C245%7C207%7C954%7C795%7C916%7C910%7C544%7C932%7C237%7C200%7C965%7C990%7C956%7C943%7C937%7C942%7C223%7C985%7C925&postalCode=M8W&skus=15463567"

headers = {
    'authority': 'www.bestbuy.ca',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4159.2 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/15463567',
    'accept-language': 'en-US,en;q=0.9'
}

bot_token = "INSERT BOT TOKEN"
bot_chat_id = "INSERT BOT CHAT ID"


def alert(bot_message):
    params = {'chat_id': bot_chat_id, 'parse_mode': 'Markdown', 'text': bot_message}
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage', params=params)
    return response.json()


def main():
    attempt = 0
    while True:
        try:
            response = requests.get(URL, headers=headers)
            response.raise_for_status()  # Raises HTTPError if request failed

            response_formatted = response.json()
            quantity = response_formatted.get('availabilities', [{}])[0].get('shipping', {}).get('quantityRemaining', 0)

            if quantity < 1:
                print(f"Time: {datetime.now()} | Attempt: {attempt}")
                attempt += 1
                time.sleep(randint(30, 60))  # Reduce server load
            else:
                print(f"🚨 {product_name} available to ship\nQuantity: {quantity}")
                alert(f"🚨 {product_name} is available to ship\nQuantity: {quantity}\n{headers['referer']}")
                time.sleep(60)  # Wait 1 minute before checking again

        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            time.sleep(120)  # Wait before retrying


if __name__ == "__main__":
    main()
