from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class GoogleFriendsEasterEgg:
    def __init__(self):
        pass
    
    def search(self, item):
        '''Input special keywords in Google Search input field.'''

        # Crawl for DOM element with custom aria-label
        search_box = driver.find_element_by_xpath('//*[@aria-label="Search"]')
        
        # Clear previous input
        search_box.clear()

        # Input string to search field
        search_box.send_keys("friends + " + item["name"])

        # Press enter
        search_box.send_keys(Keys.ENTER)

        return

    def click(self, item):
        '''Click on Easter Egg's DOM element.'''

        # Crawl for DOM element with custom data-which-friend
        easter_egg = driver.find_element_by_xpath('//*[@data-which-friend="friends_{0}"]'.format(item["name"]))

        # Click it
        easter_egg.click()

        return

# Check for current google-chrome version and 
# get latest driver for that version if not exist in cache
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open browser with full screen
driver.maximize_window()

# Go to google
driver.get('https://www.google.com/')

# Specify names and delay 
name_arr = [{ "name": "ross", "delay": 3 }, 
            { "name": "joey", "delay": 5 },
            { "name": "phoebe", "delay": 15 },
            { "name": "chandler", "delay": 13 },
            { "name": "monica", "delay": 5 },
            { "name": "rachel", "delay": 3 }]

# Create Egg object
Egg = GoogleFriendsEasterEgg()

# Play Easter Egg Games
for item in name_arr: 
    Egg.search(item)
    Egg.click(item)

    # Wait for animation
    time.sleep(item["delay"])

# Close browser
driver.close()

# Terminate webdriver session
driver.quit()
