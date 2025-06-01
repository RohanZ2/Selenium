from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

import time


if __name__ == "__main__":
    options = uc.ChromeOptions()
    
    driver = uc.Chrome(
        use_subprocess=False,
        options=options
    )
    
 
    driver.get("https://www2.hm.com/en_ca/productpage.1235448011.html")
    time.sleep(3)
    percentage = driver.find_element(By.CSS_SELECTOR,".ed5fe2.d169d4")
    print(percentage.text)


    time.sleep(20)
    driver.quit()