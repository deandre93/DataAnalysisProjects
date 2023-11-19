# Recruiting Data Scraper

## Overview
This Python script retrieves football recruiting data from the [247Sports](https://247sports.com/) website for a specified range of years. It scrapes information such as player rankings, names, positions, physical metrics, ratings, high school details, and more. The gathered data is consolidated into a single Excel file with a separate tab for each year.

## Dependencies
Make sure you have the following Python libraries installed:

- [requests](https://docs.python-requests.org/en/latest/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)

You can install these dependencies using the following command:
```bash
pip install requests beautifulsoup4 pandas numpy xlsxwriter
```

## Usage
1. Clone this repository to your local machine.
2. Ensure the required dependencies are installed (see above).
3. Run the script using the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of your Python script.

## Output
The script generates an Excel file (`recruit_data_all_years_single_tab.xlsx`) containing a tab named 'AllData.' Each row in the tab corresponds to a football recruit's data for a specific year, including rankings, player names, positions, physical metrics, ratings, high school details, and more.

## Note
- The script simulates a unique ID for each player using random integers.
- Web scraping depends on the structure of the website, and changes to the website may affect the script's functionality. If the script fails to fetch data, check the URL, network connectivity, or headers.

## Disclaimer
This script is intended for educational and personal use only. Use it responsibly and respect the terms of service of the websites you are scraping. The author is not responsible for any misuse or legal consequences arising from the use of this script.

