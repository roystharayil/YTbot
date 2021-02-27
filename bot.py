import machine
import time
from selenium.common.exceptions import NoSuchElementException

driver = machine.browser()
users = machine.getUsers('info/email.txt')

for key in users:
    value = users[key]
    
    
    #machine.signInGoogle(driver,key,value)
    machine.search(driver,'united kannoth kadavu mini tourist','google')
    time.sleep(5)
    try:
        v1 = driver.find_element_by_link_text('Videos')
        v1.click()
        
    except NoSuchElementException:
        v2 = driver.find_element_by_link_text('VIDEOS')
        v2.click()
