import requests
import urllib3
from bs4 import BeautifulSoup

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)
jobTitle = input('Enter the job title you are looking for:\n')
location = input('Enter the location for the job:\n')
def load_indeed_jobs_div(jobTitle, location):
    getVars = {'q' : jobTitle, 'l' : location, 'fromage' : 'last', 'sort' : 'date' }
    url = ('https://www.indeed.com/jobs?' + urllib3.parse.urlencode(getVars))
    page = requests.get
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# creates a Beautiful Soup object that takes page.content as its input
# html.parser --appropriate parser for HTML content
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")


# anonymous function: converts each h2 element to lowercase and checks for the substring "python"
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

            # elements = results.find_all("div", class_="card-content")
            #
            # for job_element in elements:
            #     title_element = job_element.find("h2", class_="title")
            #     company_element = job_element.find("h3", class_="company")
            #     location_element = job_element.find("p", class_="location")
            #     print(title_element.text.strip())
            #     print(company_element.text.strip())
            #     print(location_element.text.strip())
            #     print()