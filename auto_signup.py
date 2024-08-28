import time

import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

number_of_signups = 0

def gen_rand_un():
    un = "16JE00"
    un += str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    return un

while number_of_signups < 2:
        un = gen_rand_un()

        driver = webdriver.Firefox()
        url = r"https://recommend-boosts.staginghiiv.com/"
        driver.get(url)

        email = driver.find_element(By.XPATH, "//input[@name='email']")
        email.send_keys("automated+" + un + "@gmail.com")

        submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_btn.click()

        time.sleep(5)

        driver.quit()

        number_of_signups += 1
        print("No. of Signups so far: {}".format(number_of_signups))
