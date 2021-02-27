import machine
import time
from selenium.common.exceptions import NoSuchElementException
from proxy import get_proxies

proxies = get_proxies()
for proxy in proxies:
    driver = machine.browser(proxy)

users = machine.getUsers('info/email.txt')

for key in users:
    value = users[key]
    
    
    #machine.signInGoogle(driver,key,value)
    machine.search(driver,'united kannoth kadavu mini tourist','google')
    time.sleep(5)
    try:
        v1 = driver.find_element_by_link_text('Videos')
        v1.click()
        time.sleep(3)
        machine.getVideoLink()
    except NoSuchElementException:
        v2 = driver.find_element_by_link_text('VIDEOS')
        v2.click()
