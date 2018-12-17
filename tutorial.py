# coding: utf-8
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page
page.status_code
page.content
get_ipython().run_line_magic('clear', '')
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
list(soup.children)
soup.children
[type(item) for item in list(soup.children)]
html = list(soup.children)[2]
html
list(html.children)
[type(item) for item in list(html.children)]
body = list(html.children)[3]
body
list(body.children)
p = list(body.children)[1]
p
p.get_text()
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p')
soup.find_all('p')[0].get_text()
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup
soup.find_all('p', class_='outer-text')
soup.find_all(id='first')
soup.select('div p')
type(soup.select('div p'))
[type(item) for item in soup.select('div p')]
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_='tombstone-container')
tonight = forecast_items[0]
print(tonight.prettify())
tonight.find(class_="period-name").get_text()
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_test()
img = tonight.find("img")
img
desc = img["title"]
print(desc)
