from selenium import webdriver
import time, os, sys
driver = webdriver.Chrome()

from selenium.webdriver.common.by import By
driver.get('https://korean.visitkorea.or.kr/main/main.do')
driver.set_window_size(1200,700) 
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="placeHolder"]/a').click()
time.sleep(1)
driver.find_element(By.ID, 'inp_search').send_keys('여름여행'+'\n')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="sorting_options"]/button[4]/span').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="32"]/button/span').click()

time.sleep(5)
driver.close()