from selenium import webdriver

driver = webdriver.Firefox()
# Go to your page url
driver.get('http://sv.dut.udn.vn/Default.aspx')
# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
button_element = driver.find_element_by_id('linkDangNhap')
button_element.click()