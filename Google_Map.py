import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.google.com/maps/@22.4270182,87.8647865,15z")
driver.maximize_window()
time.sleep(3)

def searchplace():
    place=driver.find_element(By.XPATH,"//input[@id='searchboxinput']")
    place.send_keys("patna")
    time.sleep(3)
    search=driver.find_element(By.XPATH,"//button[@id='searchbox-searchbutton']")
    search.click()
    time.sleep(4)

searchplace()

def direction():
    time.sleep(5)
    directionkelea=driver.find_element(By.XPATH,"//img[@alt='Directions']")
    directionkelea.click()
    time.sleep(6)

direction()

def kahajanahai():
    time.sleep(5)
    kahajana=driver.find_element(By.XPATH,"//input[@placeholder='Choose starting point, or click on the map...']")
    kahajana.send_keys("golghar")
    time.sleep(4)
    search=driver.find_element(By.XPATH,"//div[@id='directions-searchbox-0']//button[@aria-label='Search']")
    search.click()

kahajanahai()

def kilometer():
    time.sleep(5)
    totalkilometer=driver.find_element(By.XPATH,"//div[@id='section-directions-trip-0']//div[@class='MespJc']//div//div[contains(text(),'3.9 km')]")
    print("Total kilometer :",totalkilometer.text)
    time.sleep(5)
    # MotorCycle=driver.find_element(By.XPATH,"//div[@id='section-directions-trip-0']//div[@class='MespJc']//div//span[contains(text(),'14 min')]")
    # print("Distance By MotorCycle:",MotorCycle.text)
    # time.sleep(5)
    # Train=driver.find_element(By.XPATH,"//span[normalize-space()='14 min']")
    # print("train distance:",Train.text)
    driver.find_element(By.XPATH,"//img[@aria-label='Transit']").click()
    time.sleep(3)



kilometer()







