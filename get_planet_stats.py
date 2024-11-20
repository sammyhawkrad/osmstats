import requests  
from bs4 import BeautifulSoup  

# URL of stats page  
url = 'https://planet.openstreetmap.org/statistics/data_stats.html'  

# Send a GET request to fetch the content of the webpage  
response = requests.get(url)  
html_content = response.text  

# Parse the HTML content using BeautifulSoup  
soup = BeautifulSoup(html_content, 'html.parser')

REPORT_RUN_AT = soup.find('h2').get_text(strip=True)
REPORT = {}
NUMBER_OF_EDITORS = []
TOP_USERS = {}


# Get report run details
table = soup.find('table')
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        REPORT[cells[0].get_text(strip=True)] = cells[1].get_text(strip=True)

# Get number of users editing over the past day, week, month
h2_number_of_editors = soup.find('h2', id='number-of-editors')
if h2_number_of_editors:
    table_number_of_editors = h2_number_of_editors.find_next('table')
    headings_number_of_editors = [th.get_text(strip=True) for th in table_number_of_editors.find('tr').find_all('th')]
    for row in table_number_of_editors.find_all('tr')[1:]:
        cells = row.find_all(recursive=False)
        if cells:
            NUMBER_OF_EDITORS.append({headings_number_of_editors[i]: cells[i].get_text(strip=True) for i in range(len(cells))})

# Get top users editing over the past day, week, month
h2_top_users = soup.find('h2', id='top-editors')
table_top_users = h2_top_users.find_next('table')

if table_top_users:
    table_data = []
    headings_top_users = [th.get_text(strip=True) for th in table_top_users.find_all('th')]

    for idx, row in enumerate(table_top_users.find_all('tr')[1:]):
        if idx >= 10:
            break
        cells = row.find_all('td')
        if cells:
            row_data = {}
            for i, cell in enumerate(cells):
                if i < len(headings_top_users):
                    row_data[headings_top_users[i]] = cell.get_text(strip=False).split(' ')
            
            if row_data:
                table_data.append(row_data)
    
    TOP_USERS = {th: [] for th in headings_top_users}
    TOP_USERS = {th: [row.get(th, '') for row in table_data] for th in headings_top_users}
    
def get_planet_stats():
    return REPORT_RUN_AT, REPORT, NUMBER_OF_EDITORS, TOP_USERS

if __name__ == "__main__":
    report_run_at, report, number_of_editors, top_users = get_planet_stats()
    print("Report Run At:", report_run_at)