from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
    driver = webdriver.Chrome()
    driver.get("http://199.116.235.229:8000/")

    name = driver.find_element_by_id("name")
    assert name != None
    
    about = driver.find_element_by_id("about")
    assert about != None
    
    skills = driver.find_element_by_id("skills")
    assert skills != None
    
    workExperience = driver.find_element_by_id("work")
    assert workExperience != None

    contactInfo = driver.find_element_by_id("contact")
    assert contactInfo != None

