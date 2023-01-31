from internet_speed_twitter_bot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = "/Users/mihaelcindori/Desktop/100_days_of_code_Python_Pro_Bootcamp_for_2022/Day_48/chromedriver"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

internet_speed = bot.get_internet_speed()

print(f"down: {bot.down}")
print(f"up: {bot.up}")

bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)

bot.driver.quit()