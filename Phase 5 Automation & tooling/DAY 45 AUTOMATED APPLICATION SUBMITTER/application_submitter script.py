from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path

driver = webdriver.Chrome()
base_folder = Path(__file__).resolve().parent
image_path = str(base_folder / "han_sohee.png")

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
wait = WebDriverWait(driver, 10)

name = driver.find_element(By.ID, "name")
name.clear()
name.send_keys("yung anikin")

e_mail = driver.find_element(By.ID, "email")
e_mail.clear()
e_mail.send_keys("yung.anikin@example.com")

male_radio = driver.find_element(By.XPATH, "//label[text()='Male']")
male_radio.click()

mobile = driver.find_element(By.ID, "mobile")
mobile.clear()
mobile.send_keys("1234567890")

date_of_birth = driver.find_element(By.ID, "dob")
date_of_birth.clear()
date_of_birth.send_keys("01-01-1990")

subject = driver.find_element(By.ID, "subjects")
subject.clear()
subject.send_keys("Maths")

sports_checkbox = driver.find_element(By.XPATH, "//label[text()='Sports']/preceding-sibling::input[1]")
if not sports_checkbox.is_selected():
    sports_checkbox.click()

file_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
file_input.send_keys(image_path)

address_box = driver.find_element(By.XPATH, "//textarea[@id='picture']")
address_box.clear()
address_box.send_keys("123 Main Street, City, Country")

state_dropdown = Select(driver.find_element(By.ID, "state"))
state_dropdown.select_by_visible_text("NCR")

city_dropdown = Select(driver.find_element(By.ID, "city"))
city_dropdown.select_by_visible_text("Agra")

login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']"))
)
login_btn.click()

driver.quit()