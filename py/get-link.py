from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

user="914199930@qq.com"
password="um123456"

driver = webdriver.Chrome()
driver.get('https://shimo.im/login')
print("正在输入用户名和密码")
driver.find_element_by_name("mobileOrEmail").clear()
driver.find_element_by_name("mobileOrEmail").send_keys(user)
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("password").send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source 
print("登录完成")  
time.sleep(3)
# -----下面才是通常的调试部分 
file ='https://shimo.im/folder/WfwlSXPeh2wqIa2I'  
driver.get(file) 
print("打开目标文件夹")
a = driver.find_element_by_class_name("sc-1s77fuj-0 bhEhNM").current_url
print(a)

