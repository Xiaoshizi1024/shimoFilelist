from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

user="914199930@qq.com"
password="xxxxxxxxx"

driver = webdriver.Chrome()
driver.get('https://shimo.im/login')
time.sleep(5)
##driver.find_element_by_xpath("./*//button[@type='submit']").click()
print("正在输入用户名和密码")
#清空登录框
driver.find_element_by_name("mobileOrEmail").clear()
#自动填入登录用户名
driver.find_element_by_name("mobileOrEmail").send_keys(user)
#清空密码框
driver.find_element_by_name("password").clear()
#自动填入登录密码
driver.find_element_by_name("password").send_keys(password)
#点击登录按钮进行登录
driver.find_element_by_name("password").send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source 
# time.sleep(10)
print("登录完成")

# driver.get('https://shimo.im/login')
# #获取cookies
# cookie_items = driver.get_cookies()

# #获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
# for cookie_item in cookie_items:
#     post[cookie_item['name']] = cookie_item['value']
# cookie_str = json.dumps(post)
# with open('cookie.txt', 'w', encoding='utf-8') as f:
#     f.write(cookie_str)
# f.close()

