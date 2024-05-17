

from gettext import install
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains        
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
import time

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#Name
driver.find_element(By.ID,"name").send_keys("RAJEEV KUMAR DAS")
time.sleep(2)

#Tabs
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("laptop")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
time.sleep(3)



