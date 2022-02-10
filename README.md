# Yugioh-Bot
Yugioh-Bot is a Python web scraper designed to pull information about yugioh cards using the [YuGiOh Prices API](https://yugiohprices.docs.apiary.io/#).

## Installation

To use the remote repository copy and paste the command below. 

```bash
git clone https://github.com/n00b110/yugioh-bot.git
```

## Usage
Make sure you have Python3 installed prior to the attempted usage of this repo. If you already have
it installed, then ```cd``` into the directory and enter the command below to install some of the dependicies for this project.

```
pip3 install requirements.txt
```
To use the webscraper follow the apporiate commands on the help screen below:
```
usage: bot.py [-h] [-r] [-i IMAGE] [-c CARD_NAME]

Web scraper for extracting yugioh card data from https://yugiohprices.com/.

optional arguments:
  -h, --help            show this help message and exit
  -r, --rising          will only return list of cards whose prices are increasing
  -i IMAGE, --image IMAGE
                        will download image as specified name to current working directory
  -c CARD_NAME, --card_name CARD_NAME
                        will only return information for card name supplied
```
So the get card data on a card like Dark Magician simply put: 
```
python3 bot.py -c "Dark Magician"
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
