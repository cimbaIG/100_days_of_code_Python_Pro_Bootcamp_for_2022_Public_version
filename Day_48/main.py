from selenium import webdriver

chrome_driver_path = "/Users/mihaelcindori/Desktop/100_days_of_code_Python_Pro_Bootcamp_for_2022/Day_48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# My Solution
event_data = driver.find_elements_by_css_selector(".event-widget ul.menu li a")
event_times = driver.find_elements_by_css_selector(".event-widget ul.menu time")

events = {}
for n in range(len(event_data) - 1):
    events.update({n: {"time": event_times[n].text, "name": event_data[n].text}})
print(events)

# Udemy solution
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.text)
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in event_names:
#     print(name.text)

# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
# print(events)

# driver.close()
driver.quit()