import requests
from bs4 import BeautifulSoup

# create User-Agent
headers = {"User-Agent": "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/31.0.1650.0 Safari/537.36"}

# passing the user agent as a parameter along with the get() Request
response = requests.get("http://pythonjobs.github.io/", headers=headers)

# Store webpage contents
webpage = response.content

# Check Status Code
print(response.status_code)
# Create BeautifulSoup object out of the webpage content
soup = BeautifulSoup(webpage, "html.parser")

# the logic
for job in soup.find_all('section', class_='job_list'):
    title = [a for a in job.find_all('h1')]
    for n, tag in enumerate(job.find_all('div', class_='job')):
        company_element = [x for x in tag.find_all('span', class_='info')]
        print("Job Title: ", title[n].text.strip())
        print("Location: ", company_element[0].text.strip())
        print("Company: ", company_element[3].text.strip())
        print()