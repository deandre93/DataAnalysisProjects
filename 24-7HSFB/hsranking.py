import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Function to extract data for a specific year
def scrape_data(year):
    url = f"https://247sports.com/Season/{year}-Football/RecruitRankings/?InstitutionGroup=HighSchool/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        ranks = [rank.text.strip() for rank in soup.select('.rank-column .primary')]
        players = [player.a.text.strip() if player.a else '' for player in soup.find_all('div', {'class': 'recruit'})]
        positions = [position.text for position in soup.find_all('div', {'class': 'position'})]
        ht_wt = [metric.text.strip() for metric in soup.find_all('div', {'class': 'metrics'})]
        
        heights = []
        weights = []
        for hw in ht_wt:
            height, weight = map(str.strip, hw.split('/'))
            heights.append(height)
            weights.append(weight)
            
        ratings = []
        for rating_div in soup.find_all('div', {'class': 'rating'}):
            score_span = rating_div.find('span', {'class': 'score'})
            if score_span:
                ratings.append(score_span.text.strip())
            else:
                ratings.append('')
        meta_info = [meta.span.text.strip() if meta.span else '' for meta in soup.find_all('div', {'class': 'recruit'})]
        high_school_names = []
        cities = []
        states = []
        for info in meta_info:
            parts = info.split('(')
            if len(parts) == 2:
                high_school_names.append(parts[0].strip())
                city_state = parts[1].replace(')', '').strip().split(', ')
                if len(city_state) == 2:
                    cities.append(city_state[0])
                    states.append(city_state[1])
                else:
                    cities.append('')
                    states.append('')
            else:
                high_school_names.append('')
                cities.append('')
                states.append('')
        
        # Add columns for 'Year' and 'ID'
        year_column = [year] * len(ranks)
        id_column = [str(np.random.randint(100_000, 1_000_000)) for _ in range(len(ranks))]
        
        data = {'Year': year_column, 'ID': id_column, 'Rank': ranks, 'Player': players, 'Position': positions,
                'Height': heights, 'Weight': weights, 'Rating': ratings, 'High School': high_school_names,
                'City': cities, 'State': states}
        
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Failed to fetch the webpage for {year}. Check the URL, network connectivity, or headers.")
        return None

# Create a single Excel file with all data in one tab
excel_file_path = 'recruit_data_all_years_single_tab.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_all_years = pd.DataFrame()
    for year in range(2014, 2025):
        df = scrape_data(year)
        if df is not None:
            df_all_years = pd.concat([df_all_years, df], ignore_index=True)


            # Convert 'Height' column values
            df_all_years['Height'] = df_all_years['Height'].apply(lambda x: f"{x.split('-')[0]}ft {x.split('-')[1]}in" if '-' in x else f"{x}ft" if 'ft' not in x else x)



    df_all_years.to_excel(writer, sheet_name='AllData', index=False)

print(f"Excel file '{excel_file_path}' created successfully.")
