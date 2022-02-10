import uuid
import os
import requests
import argparse
from PIL import Image
from shutil import copyfileobj

class Scraper:
    """
    Webscraper for scraping cards images and card data from https://yugiohprices.com either
    downloading them from into a file or simply displaying them to the screen.
    """

    def __init__(self, get_rising=True, get_img=False, card_name=None):
        self.get_img = get_img
        self.card_name = None or card_name
        self.get_rising = None or get_rising  # Makes sure that even if "get_rising" is None get rising is called by default
        self.rise_url = "http://yugiohprices.com/api/rising_and_falling"
        self.most_expensive_url = "http://yugiohprices.com/api/top_100_cards?"
        self.image_url = f"http://yugiohprices.com/api/card_image/{get_img}"
        self.search_url = f"http://yugiohprices.com/api/card_data/{card_name}"  # Response for card names is
        # different from the rising/falling lists.

    def scrape(self):
        """
        Method for scraping and retrieving data from the webiste,
        also verifies if a specific card names exist if the 'card_name' option is specificed
        """
        if self.card_name:
            response = requests.get(self.search_url)
            if response.status_code == 200:
                card_data = response.json()
                card_name = card_data['data']['name']
                text = card_data['data']['text']
                card_type = card_data['data']['card_type']
                type = card_data['data']['type']
                family = card_data['data']['family']
                atk_points = card_data['data']['atk']
                def_points = card_data['data']['def']
                card_level = card_data['data']['level']
                if card_type == "monster":
                    print(f"Name: {card_name}  \nText: {text} \nCard Type: {card_type} \nType: {type}\nFamily: {family}\n" \
                        f"Atk Points: {atk_points}\nDef Points: {def_points}")

            elif response.status_code == 400:
                print("[+] Something went wrong check if the card name supplied is correct.")

        elif self.get_rising:
            response = requests.get(self.rise_url)
            if response.status_code == 200:
                card_data = response.json()
            print(f"{'Card Name':60} {'Price':30} {'Shift':20} {'Rarity':10}")
            for data in card_data['data']['rising']:
                name = data['name']
                price = "%.2f" % data['price']
                price_shift = "%.2f" % data['price']
                rarity = data['rarity']
                print(f"{name:60} ${price:30} +{price_shift:20} {rarity:10}")

        elif self.get_img:
            response = requests.get(self.image_url, stream=True)

            if response.status_code == 200:
                filename = str(uuid.uuid4()) + '.jpg'
                filename_path = os.path.abspath(filename)
                response.raw.decode_content = True
                with open(filename, 'wb') as f:
                    copyfileobj(response.raw, f)
                print(f"[+] File: {filename} successfully written!")
                if os.path.exists(filename):
                    img = Image.open(filename_path)
                    img.show()

            else:
                print("[+] Card name not found, please check the name and try again!")




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Web scraper for extracting yugioh card data from https://yugiohprices.com/.")
    parser.add_argument('-r', '--rising', action="store_true",
                        help="will only return list of cards whose prices are increasing")
    parser.add_argument('-i', '--image', action="store",
                        help="will download image as specified name to current working directory")
    parser.add_argument('-c', '--card_name', action="store", help="will only return information for card name supplied")
    args = parser.parse_args()
    scraper = Scraper(args.rising, args.image, args.card_name)
    scraper.scrape()
