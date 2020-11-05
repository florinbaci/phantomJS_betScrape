from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from time import gmtime, strftime
import time
sites = ['https://ls.betradar.com/']
for url in sites:
    r = requests.get(url)
    page_source = r.text
    page_source = page_source.split('\n')
    print("\nURL:", url)
    print("--------------------------------------")
    # print the first five lines of the page source
    for row in page_source[:]:
        print(row)
    print("--------------------------------------")

'''# Getting the source of the webpage and storing it as Text
driver = webdriver.Chrome(executable_path='C:/Users/User/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe')
driver.maximize_window()
url = "https://ls.betradar.com/"
driver.get(url)
a = driver.page_source
name = 'a1.txt'
try:
    file = open(name, 'w', encoding='utf-8')
    file.write(a)
    print(a)
    file.close()

except:
    print('page' + str(x) + '\n')

a = ""
time.sleep(3)

print(a)

driver.close()'''