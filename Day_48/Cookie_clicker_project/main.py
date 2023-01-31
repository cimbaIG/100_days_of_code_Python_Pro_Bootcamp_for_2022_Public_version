from selenium import webdriver
import time

chrome_driver_path = "/Users/mihaelcindori/Desktop/100_days_of_code_Python_Pro_Bootcamp_for_2022/Day_48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

def create_elements():
    cookie = driver.find_element_by_id("cookie")
    money = driver.find_element_by_id("money")
    cursor = driver.find_element_by_id("buyCursor")
    grandma = driver.find_element_by_id("buyGrandma")
    factory = driver.find_element_by_id("buyFactory")
    mine = driver.find_element_by_id("buyMine")
    shipment = driver.find_element_by_id("buyShipment")
    alchemy_lab = driver.find_element_by_id("buyAlchemy lab")
    portal = driver.find_element_by_id("buyPortal")
    time_machine = driver.find_element_by_id("buyTime machine")
    return cookie, money, cursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine

def check_cookie_number():
    return int(create_elements()[1].text.replace(",",""))

def update_cookie_numbers():
    cursor_num = int(driver.find_element_by_css_selector("#buyCursor b").text.split(" ")[2].replace(",",""))
    grandma_num = int(driver.find_element_by_css_selector("#buyGrandma b").text.split(" ")[2].replace(",",""))
    factory_num = int(driver.find_element_by_css_selector("#buyFactory b").text.split(" ")[2].replace(",",""))
    mine_num = int(driver.find_element_by_css_selector("#buyMine b").text.split(" ")[2].replace(",",""))
    shipment_num = int(driver.find_element_by_css_selector("#buyShipment b").text.split(" ")[2].replace(",",""))
    alchemy_num = int(driver.find_element_by_xpath("//*[@id='buyAlchemy lab']").text.split(" ")[3].split("\n")[0].replace(",", ""))
    portal_num = int(driver.find_element_by_css_selector("#buyPortal b").text.split(" ")[2].replace(",",""))
    time_num = int(driver.find_element_by_xpath("//*[@id='buyTime machine']").text.split(" ")[3].split("\n")[0].replace(",", ""))
    return cursor_num, grandma_num, factory_num, mine_num, shipment_num, alchemy_num, portal_num, time_num

def check_right_pane():
    if update_cookie_numbers()[7] <= check_cookie_number():
        create_elements[9]
    elif update_cookie_numbers()[6] <= check_cookie_number():
        create_elements[8]
    elif update_cookie_numbers()[5] <= check_cookie_number():
        create_elements()[7].click()
    elif update_cookie_numbers()[4] <= check_cookie_number():
        create_elements()[6].click()
    elif update_cookie_numbers()[3] <= check_cookie_number():
        create_elements()[5].click()
    elif update_cookie_numbers()[2] <= check_cookie_number():
        create_elements()[4].click()
    elif update_cookie_numbers()[1] <= check_cookie_number():
        create_elements()[3].click()
    elif update_cookie_numbers()[0] <= check_cookie_number():
        create_elements()[2].click()

start_time = time.time()
seconds = 300

while True:
    current_time = time.time()
    elapsed_time = int(current_time - start_time)

    create_elements()[0].click()

    if (elapsed_time % 5 != 0):
        check_pane = True 
    if (elapsed_time % 5) == 0 and (elapsed_time != 0):
        if check_pane:
            check_right_pane()
            check_pane = False

    if elapsed_time >= seconds:
        cookies_per_second = driver.find_element_by_id("cps").text.replace(",", "")
        print("Finished iterating in: " + str(elapsed_time)  + " seconds")
        print("Cookies/second:", cookies_per_second)
        driver.quit()
        break

# New implementation for time handling
timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    create_elements()[0].click()

    if time.time() > timeout:
        check_right_pane()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_per_second = driver.find_element_by_id("cps").text.replace(",", "")
        print("Finished iterating in: " + str(elapsed_time)  + " seconds")
        print("Cookies/second:", cookies_per_second)
        driver.quit()
        break

# Old implementation for time handling
# start_time = time.time()
# seconds = 300

# while True:
#     current_time = time.time()
#     elapsed_time = int(current_time - start_time)

#     create_elements()[0].click()

#     if (elapsed_time % 5 != 0):
#         check_pane = True 
#     if (elapsed_time % 5) == 0 and (elapsed_time != 0):
#         if check_pane:
#             check_right_pane()
#             check_pane = False

#     if elapsed_time >= seconds:
#         cookies_per_second = driver.find_element_by_id("cps").text.replace(",", "")
#         print("Finished iterating in: " + str(elapsed_time)  + " seconds")
#         print("Cookies/second:", cookies_per_second)
#         driver.quit()
#         break