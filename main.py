from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


browser=webdriver.Chrome()
url='https://www.jd.com/'

try:
    browser.get(url)
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    browser.get(url)

    inputkw=browser.find_element_by_id('key')
    inputkw.send_keys('华为')
    inputkw.clear()
    inputkw.send_keys('华为 mate9')
    time.sleep(3)
    inputkw.send_keys(Keys.ENTER)
    time.sleep(5)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
finally:
    wait=WebDriverWait(browser,10)
    nextpage=wait.until(EC.presence_of_element_located((By.XPATH,'//a[@class="fp-next"]')))
    items=browser.find_elements_by_xpath('//div[@class="gl-i-wrap"]')
    i=0
    print(len(items))
    for item in items:
#        yield{
#            "price":item.find_element_by_xpath('//div[@class="p-price"]/strong/i').text,
#            "descript":item.find_element_by_xpath('//div[@class="p-name"]//em').text,
#            "judge":item.find_element_by_xpath('//div[@class="p-commit"]/strong/a').text
#        }
#
        price=item.find_element_by_css_selector(".p-price").text
        des=item.find_element_by_class_name("p-name").text
        print(price,des)
#        i=i+1
#        print(str(i))
browser.close()
browser.switch_to_window(browser.window_handles[0])
browser.close()
