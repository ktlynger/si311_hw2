import csv
import requests
from bs4 import BeautifulSoup

"""

Scrapping Michigan Softball 2024 Data and then putting it in a list of lists.

"""
URL = "https://mgoblue.com/sports/softball/stats/2024"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('table')
rows = table.find_all('tr', class_='stat_meets_min')
headers = [header.text.strip() for header in table.find_all('th', class_='text-center')]
headers[0] = 'Name'

michigan_softball_data = []
michigan_softball_data.append(headers)

for row in rows:
    cols = row.find_all('td')
    full_name_lst = row.find('a', class_='hide-on-medium-down').text.strip().split(',')
    full_name = f"{full_name_lst[1].strip()} {full_name_lst[0]}"
    cols = [col.text.strip() for col in cols]
    cols[0] = full_name
    michigan_softball_data.append(cols[:-1])

print(michigan_softball_data)


"""

Writing data in a csv file.

"""

with open('michigan_softball_2024_data.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(michigan_softball_data)

print("CSV file written successfully.")

"""

I commented out the code because I already successfully wrote the csv file

"""