# carousell-item-scraper

An asynchronous Python web scraper built with Playwright to extract product listings from Carousell Malaysia. It automates the search process, loads all available results, and exports the data into a clean CSV file.

## Features

* **Asynchronous Execution:** Fast and efficient scraping using `asyncio` and `playwright.async_api`.
* **Bot Evasion:** Utilizes `playwright-stealth` to bypass basic bot detection mechanisms.
* **Automated Pagination:** Automatically handles UI pop-ups and clicks "Show more results" to fetch all available items for a search query.
* **Resource Optimization:** Aborts image loading (PNG, JPG, SVG, GIF) to speed up page load times and reduce bandwidth usage.
* **CSV Export:** Neatly formats and exports scraped data (Product Name, Price, and Link) into a CSV file.

## Prerequisites

* Python 3.7 or higher
* pip (Python package installer)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/liq-0708/carousell-item-scraper.git
   cd carousell-item-scraper
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the required Playwright browsers (Chromium):
   ```bash
   playwright install chromium
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. When prompted in the terminal, enter the product name you wish to search for on Carousell Malaysia.

3. A visible browser window will open to perform the scraping. Once completed, a CSV file named `carousell_data_<your_search_term>.csv` will be generated in the root directory.

## Disclaimer

This tool is provided for educational purposes only. Please adhere to Carousell's Terms of Service regarding automated scraping and rate limiting before using this script extensively.