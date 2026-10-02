from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = uc.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/")


wait = WebDriverWait(driver, 15)
language_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
language_button.click()

big_cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
cookie_count = wait.until(EC.element_to_be_clickable((By.ID, "cookies")))

timeout = time.time() + 5
five_min = time.time() + 60 * 5
cookie_upgrades = {}
while True:
    big_cookie.click()
    if time.time() > timeout:
        cookie_upgrades = {}
        affordable_upgrades = driver.find_elements(By.CSS_SELECTOR, "#store .product.unlocked.enabled")
        for item in affordable_upgrades:
            price_element = item.find_element(By.CLASS_NAME, "price")
            price = int(price_element.text.replace(",", ""))
            cookie_upgrades[price] = item
        
        if cookie_upgrades:
            highest_affordable_price = max(cookie_upgrades.keys())
            item_to_buy = cookie_upgrades[highest_affordable_price]
            item_to_buy.click()
            
        timeout = time.time() + 5    
            
        if time.time() > five_min:
            print("5 minutes reached, stopping the bot.")
            break
driver.quit()