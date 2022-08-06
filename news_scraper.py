import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.politifact.com/factchecks/list/?page='+str(page)
try:
    #Use the browser to get the URL. This is a suspicious command that might blow up.
    page = requests.get(url)
except Exception as e:
    # get the exception information
    error_type, error_obj, error_info = sys.exc_info()

    # print the link that cause the problem
    print('ERROR FOR LINK:', url)

    # print error info and line that threw the exception
    print(error_type, 'Line:', error_info.tb_lineno)
    page.status_code
    # continue
    #this is a test