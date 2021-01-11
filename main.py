from selenium import webdriver
import selenium.common.exceptions

chrome_options = webdriver.ChromeOptions( )
# 设置好应用扩展
extension_path = '/Users/rockontrol/Desktop/grade/ietab.crx'
chrome_options.add_extension(extension_path)
# 启动浏览器，并设置好wait
browser = webdriver.Chrome('/Users/rockontrol/Desktop/grade/chromedriver',chrome_options=chrome_options)
# driver = webdriver.Chrome('/Users/rockontrol/Desktop/grade/chromedriver')
browser.get('http://119.6.110.96:8088/loginAction.do')
