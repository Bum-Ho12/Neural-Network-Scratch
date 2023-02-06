from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from random_user_agent.user_agent import UserAgent
# from random_user_agent.params import SoftwareName, OperatingSystem
from random_latency import RandomLatency
from random_sleep import RandomSleep
# https://github.com/CryptoidCoder/selenium-Ad-Clicker
# specify the website URL
url = "https://www.denmpro.com"

# create an instance of the Chrome browser in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument(f'user-agent={UserAgent().chrome}')

driver = webdriver.Chrome(chrome_options=chrome_options)
rl = RandomLatency(driver)
rs = RandomSleep()
wait = WebDriverWait(driver, 10)

for _ in range(9):
    # load the website
    driver.get(url)
    rl.add_random_latency()
    rs.random_sleep()

    # Wait for the ad-link element to be present and clickable
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ad-link")))
    ActionChains(driver).move_to_element(element).click(element).perform()
    rl.add_random_latency()
    rs.random_sleep()

    # Wait for the back button to be present and clickable
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.back-button")))
    ActionChains(driver).move_to_element(element).click(element).perform()
    rl.add_random_latency()
    rs.random_sleep()

    # Wait for the second ad-link element to be present and clickable
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ad-link:nth-child(2)")))
    ActionChains(driver).move_to_element(element).click(element).perform()
    rl.add_random_latency()
    rs.random_sleep()

    # Wait for the back button to be present and clickable
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.back-button")))
    ActionChains(driver).move_to_element(element).click(element).perform()
    rl.add_random_latency()
    rs.random_sleep()

# close the browser
driver.quit()