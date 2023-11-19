import requests
from bs4 import BeautifulSoup
import csv

# Get the NFL passing stat year from the user
nfl_year = input("Enter the NFL passing stat year (e.g., 2020): ")

# Construct the URL based on the user input
url = f"https://www.pro-football-reference.com/years/{nfl_year}/passing.htm"

# Send an HTTP GET request to fetch the webpage content
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table that contains the data
    table = soup.find("table")

    # Find all rows in the table body
    rows = table.find_all("tr")

    # Initialize a list to store scraped data
    scraped_data = []

    # Loop through each row and extract the data from the specified columns
    for row in rows:
        if row.has_attr("class") and "thead" in row["class"]:
            continue  # Skip rows with class name 'thead'

        columns = row.find_all(["td", "th"], class_=["left", "right"])

        try:
            if len(columns) >= 31:  # Check if the row has enough columns
                player_data = []
                for column in columns:
                    player_data.append(column.get_text())

                # Append the extracted data to the list
                scraped_data.append(player_data)

        except Exception as e:
            print("An error occurred:", e)

    # Specify the CSV file path
    csv_file_path = f"nfl_passing_data{nfl_year}.csv"

    # Specify the field names (column headers) for the CSV file
    field_names = [
        "Rk", "Player", "Tm", "Age", "Pos", "G", "GS", "QBrec", "Cmp", "Att", "Cmp%", "Yds",
        "TD", "TD%", "Int", "Int%", "1D", "Succ%","Lng", "Y/A", "AY/A", "Y/C", "Y/G", "Rate", "QBR",
        "Sk", "Yds", "Sk%", "NY/A", "ANY/A", "4QC", "GWD"
    ]

    # Write the data to the CSV file
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header
        writer.writerow(field_names)

        # Write the data rows
        writer.writerows(scraped_data)

    print(f"CSV file for NFL passing stats in {nfl_year} created successfully.")

else:
    print("Failed to fetch the webpage. Check the URL or network connectivity.")
