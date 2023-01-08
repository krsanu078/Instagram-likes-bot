from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass

class Instagram:
    def __init__(self):
        x=0
        service_obj = Service(r"C:\Users\skuma183\Pictures\chromedriver_win32.exe")
        self.driver=webdriver.Chrome(service=service_obj)
        self.driver.get("https://www.instagram.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.NAME, "username").send_keys(Username)
        self.driver.find_element(By.NAME, "password").send_keys(Password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(10)

        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, '//button[text()="Not now"]')).perform()
        action.click(self.driver.find_element(By.XPATH, '//button[text()="Not now"]')).perform()

        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')).perform()
        action.click(self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')).perform()

        self.driver.find_element(By.XPATH, '//span[text()="Search"]').click()
        self.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(Promotion_id)
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, f'//div[text()=\"{Promotion_id}\"]').click()
        time.sleep(20)

        self.driver.implicitly_wait(2)
    
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, '//article[@class="x1iyjqo2"]/div/div/div[2]')).perform()
        #action.click(self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')).perform()
        pic=self.driver.find_element(By.XPATH, '//article[@class="x1iyjqo2"]/div/div')
        pics=pic.find_elements(By.XPATH,'//div[@class="_aabd _aa8k _aanf"]')
        for i in pics:
            i.click()
            self.driver.implicitly_wait(2)

            like_button=self.driver.find_element(By.XPATH, '//span[@class="_aamw"]/button')
            like_button.click()
            
            close_button=self.driver.find_element(By.XPATH,'//div[@class="x78zum5 x6s0dn4 xl56j7k xdt5ytf"]')
            close_button.click()
            x=x+1
        print("Total no. of posts liked : ",x)

        

Username=input("Phone number, username or email address ")
Password=getpass.getpass()
Promotion_id=input("Enter instagram id of person whose post you want to like: ")
obj=Instagram()




