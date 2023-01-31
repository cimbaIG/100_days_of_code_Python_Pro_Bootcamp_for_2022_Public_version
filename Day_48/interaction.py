from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/mihaelcindori/Desktop/100_days_of_code_Python_Pro_Bootcamp_for_2022/Day_48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # article_num = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# # print(article_num.text)

# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()

# view_source = driver.find_element_by_link_text("View source")
# # view_source.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# My Solution
driver.get("http://secure-retreat-92358.herokuapp.com")

fname = driver.find_element_by_name("fName")
fname.send_keys("Mihael")
lname = driver.find_element_by_name("lName")
lname.send_keys("Cindori")
email = driver.find_element_by_name("email")
email.send_keys("")

btn = driver.find_element_by_css_selector("form button")
btn.click()