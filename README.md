# Genshin Scraper
an automated genshin wiki web scraping cli script.

## Features
- character, weapon and artifact json data
- character, weapon and artifact image files

# Getting Started
```bash
git clone https://github.com/lambdv/genshin-scraper
cd genshin-scraper
pip install -r requirements.txt
python cli.py update # scrap all json and image data
python cli.py compile # produce a characters, weapons and artifacts master json file from individual json files 
```