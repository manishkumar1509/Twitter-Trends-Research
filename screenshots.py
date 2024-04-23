from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import datetime
import time

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists and if it doesn't exist, download it automatically, then add chromedriver to path

def take_screenshot(url, output_file):
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")  # Run headless Chrome
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.set_window_size(1500, 1200)
    #driver.maximize_window()
    # Wait for the page to load (you can adjust the sleep time as needed)
    time.sleep(3)
    print('starting screenshot')
    driver.get_screenshot_as_file(output_file)                                                                                                          

    print('screenshot taken')
    driver.quit()

if __name__ == "__main__":
    timestamp = datetime.datetime.now()
    output_file_name = 'results/India/screenshot_'+ str(timestamp) + '.png'
    take_screenshot("https://getdaytrends.com/india/", output_file_name)