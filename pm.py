from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config.config as conf

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(conf.URL)

email_input = driver.find_element(By.NAME, "email")
email_input.clear()
email_input.send_keys(conf.email)

password_input = driver.find_element(By.NAME, "password")
password_input.clear()
password_input.send_keys(conf.password)

login_button = driver.find_element(By.XPATH, "//*[@id='signin']/form/button")
login_button.click()

project = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[3]/div/div[2]/table/tbody/tr[1]/td[2]/div"))
)
project.click()

insert_ticket_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/button"))
)
insert_ticket_button.click()

#ticket data  -> in-progress
title_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[1]/div/input")
assign_to_selector = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[2]/div/div/div/div[1]/div[2]/div/svg")

assign_to_selector.click()
