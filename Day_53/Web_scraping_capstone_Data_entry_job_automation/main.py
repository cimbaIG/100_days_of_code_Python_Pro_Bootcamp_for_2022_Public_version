import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.67022170019531%2C%22east%22%3A-122.19643629980469%2C%22south%22%3A37.68296846534594%2C%22north%22%3A37.86749929531124%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
form_url = ""
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "Accept-Language": "hr-HR,hr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# Get rental url and address data
rental_listing = soup.select(".list-card-top a")

# Get price data
prices = soup.select(".list-card .list-card-price")

rental_urls = []
for rental in rental_listing:
    if not "https://www.zillow.com" in rental["href"]:
        rental["href"] = "https://www.zillow.com" + rental["href"]
    rental_urls.append(rental["href"])
print(rental_urls)

rental_prices = [price.text.replace("/mo", "").replace("+ 1 bd", "") for price in prices]
print(rental_prices)

rental_addresses = []
for rent in rental_listing:
    img = rent.find("img", alt=True)
    rental_addresses.append(img["alt"])
print(rental_addresses)

# Fill in google form using Selenium
chrome_driver_path = "/Users/mihaelcindori/Desktop/100_days_of_code_Python_Pro_Bootcamp_for_2022/Day_48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(form_url)
time.sleep(3)

for i in range(len(rental_addresses)):
    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    address_input.send_keys(rental_addresses[i])
    price_input.send_keys(rental_prices[i])
    url_input.send_keys(rental_urls[i])
    submit_button.click()
    driver.back()
    time.sleep(3)

driver.quit()