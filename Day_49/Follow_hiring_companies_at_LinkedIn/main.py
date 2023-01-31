import time
from selenium import webdriver

LINKEDIN_MAIL = ""
LINKEDIN_PASSWORD = ""

chrome_driver_path = "/Users/mihaelcindori/Desktop/100_days_of_code_Python_Pro_Bootcamp_for_2022/Day_48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3041933712&f_AL=true&geoId=102738269&keywords=python%20developer&location=Zagreb%2C%20Croatia")

time.sleep(5)

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

# Waiting for 5 seconds to allow page to load
time.sleep(5)

# After 5 seconds the code below is executed
input_mail = driver.find_element_by_id("username")
input_password = driver.find_element_by_id("password")
input_mail.send_keys(LINKEDIN_MAIL)
input_password.send_keys(LINKEDIN_PASSWORD)
sign_in_key = driver.find_element_by_css_selector(".login__form_action_container  .btn__primary--large")
sign_in_key.click()

# Wait for 2 seconds to allow page to load completely
time.sleep(15)

# jobs = driver.find_elements_by_css_selector(".jobs-search-results ul .job-card-list__title")

i = 0
continue_following = True
while continue_following:
    # Get all companies that are currently hiring
    companies = driver.find_elements_by_css_selector(".jobs-search-results ul .job-card-container__company-name")

    companies[i].click()
    time.sleep(2)
    follow_button = driver.find_element_by_class_name("org-company-follow-button")

    if follow_button.get_attribute("aria-pressed") == "false":
        follow_button.click()
    
    driver.back()
    time.sleep(5)

    i += 1
    if i == len(companies) - 1:
        continue_following = False

driver.quit()