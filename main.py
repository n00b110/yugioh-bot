import requests
import json


class Scraper:
    """
    Webscraper for scraping cards images and card data from https://yugiohprices.com either
    downloading them from into a file or simply displaying them to the screen.
    """
    def __init__(self):
        self.rise_url = "http://yugiohprices.com/api/rising_and_falling"
        self.most_expensive_url = "http://yugiohprices.com/api/top_100_cards?"


    def scrape(self):
        """
        Method for scraping and retrieving data from the webiste,
        also verifies if a specific card names exist if the 'search_name' option is specificed
        """
        response = requests.get(self.most_expensive_url)
        if response.status_code == 200:
            card_data = response.json()

            print(f"{'Card Name':40} {'Price':30} {'Shift':20} {'Rarity':10}")
            for data in card_data['data']:
                name = data['name']
                price = "%.2f" % data['price']
                price_shift = "%.2f" % data['price']
                rarity = data['rarity']
                print(f"{name:40} ${price:30} +{price_shift:20} {rarity:10}")






card_scraper = Scraper()
card_scraper.scrape()