import requests
import urllib
from bs4 import BeautifulSoup

jobTitle = input('Enter the job title you are looking for:\n')
location = input('Enter the location for the job:\n')
qual = input('Enter the languages you are proficient in:\n')
def load_indeed_jobs_div(jobTitle, location):
    global job_soup
    getVars = {'q' : jobTitle, 'l' : location, 'fromage' : 'last', 'sort' : 'date' }
    url = ('https://www.indeed.com/jobs?' + urllib.parse.urlencode(getVars))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    job_soup = soup.find(id="resultsCol")
    return job_soup
# def extract_qualifications(job_elem):
#     qualifications = job_elem.find()
load_indeed_jobs_div(jobTitle, location)
job_elem = job_soup.find_all('div', class_='cardOutline tapItem')
print(job_elem)