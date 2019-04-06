## 今日主题  
实现石墨登录的功能     
## 践行之路  
### 利用`selenium`中的`Webdriver`来解决
尝试着利用 [爬虫需要登陆怎么办？这份python登陆代码请收下 - 知乎](https://zhuanlan.zhihu.com/p/39810121)这个方法来尝试着的行动  
- 作者提供的源代码：链接：<https://pan.baidu.com/s/1kWM0_TRVO4YAP8gMn5f5OQ>  密码：tw49    
- 学习selenium的文档  
    - 非官方-[Selenium with Python中文翻译文档 — Selenium-Python中文文档 2 documentation](https://selenium-python-zh.readthedocs.io/en/latest/index.html)  


### 围绕目标行动 
1. 安装selenium   
> 参考资料：[1. 安装 — Selenium-Python中文文档 2 documentation](https://selenium-python-zh.readthedocs.io/en/latest/installation.html#python-bindings-for-selenium)  

在cmd中输入：`pip install selenium`
``` 
C:\Users\Leo40>pip install selenium
Collecting selenium
  Downloading https://files.pythonhosted.org/packages/80/d6/4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/selenium-3.141.0-py2.py3-none-any.whl (904kB)
    100% |████████████████████████████████| 911kB 23kB/s
Requirement already satisfied: urllib3 in c:\ide\python37\lib\site-packages (from selenium) (1.24.1)
Installing collected packages: selenium
Successfully installed selenium-3.141.0 
``` 
**检测**：是否能够正常的运行  
在cmd中加载python,并且运行`from selenium import webdriver`  
收到反馈的内容为空,说明能够正常的运行  
2. 安装Chromedriver  
由于想要用Chore来调用这个功能,所以需要按照这个东西  
下载链接: [Downloads - ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)    
当前电脑Chore 版本为:73.0.3683.68,所以下载该版本的  

那么引发了另一个问题**Q:如何利用程序调用Chromedriver?**,**Chromedriver要放在哪里?是否要加入环境变量中?**  
暂时先不解决,开始看程序 

2. 利用提供的案例来演示  
运行代码  
``` python  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```    

系统进行如下反馈:   

```
PS C:\Hacker\Python\101> python -u "c:\Hacker\Python\101\ch12\selenium_demo.py"
Traceback (most recent call last):
  File "C:\IDE\python37\lib\site-packages\selenium\webdriver\common\service.py", line 76, in start
    stdin=PIPE)
  File "C:\IDE\python37\lib\subprocess.py", line 775, in __init__
    restore_signals, start_new_session)
  File "C:\IDE\python37\lib\subprocess.py", line 1178, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] 系统找不到指定的文件。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\Hacker\Python\101\ch12\selenium_demo.py", line 4, in <module>
    driver = webdriver.Firefox()
  File "C:\IDE\python37\lib\site-packages\selenium\webdriver\firefox\webdriver.py", line 164, in
__init__
    self.service.start()
  File "C:\IDE\python37\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
```   
哈哈,开心我竟然猜对了,原来是Chrome的环境没有配置好, 没有将`Chromedriver`安装到系统环境中...  
还有个问题, 我在哪里看到了Firefox应该不需要安装系统环境,但是利用Firefox不配置环境还是不能正常运行      

成功运行的反馈是:  
`DevTools listening on ws://127.0.0.1:49316/devtools/browser/b4f00645-10ef-4bbd-8cd9-d4afb2560bc6 `  

## 尝试着运用`selenium`登录shimo.im  
通过官方的内容,以及能够实现自动输入石墨的账户跟密码了,但是在点击确定进行提交时,出现了找不对这个对象的问题~  
本次运行的源码:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

user="914199930@qq.com"
password="xxxxxxxxxxxxxxxxxx"  # 请输入账户的密码

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

# time.sleep(8)
#点击登录按钮进行登录
## driver.find_element_by_xpath("./*//button[@name='loginsubmit']").click()
driver.find_element_by_class_id('geetestCapcha').send_keys
assert "No results found." not in driver.page_source 
# time.sleep(10)
```  
反馈是:  
```
Traceback (most recent call last):
  File "c:\Users\Leo40\Downloads\login.py", line 26, in <module>
    driver.find_element_by_class_id('geetestCapcha').send_keys
AttributeError: 'WebDriver' object has no attribute 'find_element_by_class_id'
```    
属性错误:WebDriver的对象没有属性“find_element_by_class_id” 
在源码中提交的源码为:  
```html
<div id="geetestCaptcha"></div>
<button class="sm-button submit sc-1n784rm-0 bcuuIb" type="black">立即登录</button>
```  
通过了解源码,修改代码再次测试
```python
#点击登录按钮进行登录
driver.find_element_by_class_name('sm-button submit sc-1n784rm-0 bcuuIb').send_keys
assert "No results found." not in driver.page_source 
print("登录完成")
```
系统进行的反馈是:
```
Traceback (most recent call last):
  File "c:\Users\Leo40\Downloads\login.py", line 26, in <module>
    driver.find_element_by_class_name('sm-button submit sc-1n784rm-0 bcuuIb').send_keys
  File "C:\IDE\python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 564, in find_element_by_class_name
    return self.find_element(by=By.CLASS_NAME, value=name)
  File "C:\IDE\python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "C:\IDE\python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\IDE\python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.InvalidSelectorException: Message: invalid selector: Compound class names not permitted
``` 
分析反馈中的问题: 

尝试用CSS选择器定位~
修改代码为: 
`driver.find_element_by_css_selector('sm-button submit sc-1n784rm-0 bcuuIb').send_keys `
还是错误,终于找到原因了,还是Html语法不了解导致的,`<button class="sm-button submit sc-1n784rm-0 bcuuIb" type="black">立即登录</button>`这个语法是调整样式的...  
详情了解可以参考: [Bootstrap 按钮 | 菜鸟教程](http://www.runoob.com/bootstrap/bootstrap-buttons.html) 
我为什么会找到这个呢?
- 由于问题解决不了, 我谷歌`button class`了, 然后第一个就是上面的网站~

在 190406 0:40:30 在上面已经得知了那个按钮没有没有实体;然后有自己尝试了一下再登录网站中直接点击`回车`就可以进行登录了,所以瞬间跳出这个坑了... 
然后尝试着在 密码行按`回车`进行登录;并且修改登录的代码为:  
` driver.find_element_by_name("password").send_keys(Keys.RETURN)` 
测试,发现登录进行了 今天的任务完成了 

及时反思: 
陷入编程问题中及时反思:
1. 这个点我理解的对吗?
2. 我有没有陷入细节呢?扩大点反馈进行输入对吗?

今日任务完成时间: 190406 0:52:05  
小狮子真是太棒了  

### 明天任务:   

1. 进入自己想要爬去的页面
2. 访问内部的文件并且获取其连接&标题名
3. 遍历该文件夹中的所以文件&文件夹
Over~

1. 如何给用户设置参数来输入 账户,密码,要爬取的石墨文件夹~
2. 如何将程序进行封装?
3. 如何将程序上线成一个网站?






## logging  
190404 16:45:09 - 17:57:52 没有实现上述目标的实现,基本上上手了`selenium` 
190405 22:35:34 - 0:51:40    尝试着运用`selenium`登录shimo.im;