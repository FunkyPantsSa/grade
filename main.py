from selenium import webdriver
import selenium.common.exceptions
import sys
import io

#usragent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
chrome_options = webdriver.ChromeOptions( )
# 设置好应用扩展
extension_path = '/Users/rockontrol/Desktop/grade/ietab.crx'
chrome_options.add_extension(extension_path)
# 启动浏览器，并设置好wait
browser = webdriver.Chrome('/Users/rockontrol/Desktop/grade/chromedriver',chrome_options=chrome_options)
# driver = webdriver.Chrome('/Users/rockontrol/Desktop/grade/chromedriver')
#browser.get('http://119.6.110.96:8088/loginAction.do')
#http://119.6.110.96:8088/loginAction.do
browser= webdriver.Chrome('chrome-extension://hehijbfgiekmjfkfjpbkbammjbdenadd/nhc.htm#url=http://119.6.110.96:8088/loginAction.do')
