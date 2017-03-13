from selenium import webdriver

browser = webdriver.Firefox(executable_path="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

browser.get('http://localhost:8000')

assert 'Django' in browser.title
