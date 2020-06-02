import requests
from bs4 import BeautifulSoup

# Send a request to Monster webpage
URL = 'https://www.monster.com/jobs/search/?q=software-engineer&where=Seattle__2C-WA'
response = requests.get(URL)
# print(dir(response))

# Extract content
content = response.content

# Convert to BS object
soup = BeautifulSoup(content, 'html.parser')

# Find an element
results = soup.find(id='SearchResults')
# print(results.prettify())

jobs_list = results.find_all('section', class_='card-content')
# print(len(jobs_list))


final_results = []

for job in jobs_list:

    job_dict = {'title': '', 'location':'', 'company':''}

    found_title = job.find('h2', class_='title')
    if found_title:
        title = found_title.text.strip()
        job_dict['title'] = title

    found_location = job.find('div', class_='location')
    if found_location:
        location = found_location.text.strip()
        job_dict['location'] = location

    found_company = job.find('div', class_='company')
    if found_company:
        company = found_company.text.strip()
        job_dict['company'] = company

    final_results.append(job_dict)

    # print(title)
    # print('********************************')
    # print(location)
    # print('********************************')
    # print(company)
    # print('\n ############################# \n')

print(final_results)

