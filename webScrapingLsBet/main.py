import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
from bs4 import BeautifulSoup
import lxml


driver = webdriver.Chrome(executable_path='C:/Users/User/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe')#(options=options)

driver.get("https://ls.betradar.com/")

# Let the code on their end run
#time.sleep(3)

pageSource = driver.page_source

# Let the code on their end run
time.sleep(15)

print(pageSource)



#x = driver.find_element_by_tag_name('html')

#print(x)




# Save it to a variable
#html = driver.page_source
#driver.quit()

# And then just paste it right back into beautifulsoup!
#projects_soup = BeautifulSoup(html, 'lxml')


#r = requests.get('https://ls.betradar.com/')

#soup = BeautifulSoup(r.text, 'html.parser')

#print(r.text[0:1000])

#print(soup)





