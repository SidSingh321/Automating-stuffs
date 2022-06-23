import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
file_path = os.path.dirname(sys.executable)

# getting date in formatA
extract_time = datetime.now()
month_day_year = extract_time.strftime("%m%d%Y")

website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\Siddharth\Desktop\chromedriver_win32\chromedriver"

# Creating the driver
# adding headless-mode
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# Finding Elements

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to the same folder where the executable will be located
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df = pd.DataFrame(my_dict)

file_name = f'extracted_data_{month_day_year}.csv'
final_path = os.path.join(file_path, file_name)
df.to_csv(final_path)

driver.quit()