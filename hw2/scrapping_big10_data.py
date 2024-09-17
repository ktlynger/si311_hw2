# CHECK THAT YOU GOT ALL THE DATA

# Using the notebook to scrap big ten data 
import csv
import requests
from bs4 import BeautifulSoup

URL = "https://d1softball.com/conference/big-ten-conference/2024/statistics/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

#print(soup.prettify())

# the code below gets the headings for the data in the table
table = soup.find('table')
headers = [header.text.strip() for header in table.find_all('th')]

# the code below gets the data for the table
data_body = soup.find('div', class_='dataTables_scrollBody')
table = soup.find('table')
rows = table.find_all('tr')

big10_data = []
big10_data.append(headers[1:])

for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    if cols != []:
        big10_data.append(cols[1:])

""" I commented out the code before because I already created the csv with the data"""
# putting the data in a csv file 
# with open('big10_data.csv', mode='a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(big10_data)

# print("CSV file written successfully.")