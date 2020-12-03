from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
## url에 접근한다.
driver.get('https://finance.naver.com/item/main.nhn?code=005930')




elem = driver.find_element_by_class_name('no_up')
 
print(elem.text)