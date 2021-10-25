from selenium import webdriver

chrome_driver = webdriver.Chrome(executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4"
                                                 "\\chromedriver_win32\\chromedriver.exe")
gecko_driver = webdriver.Firefox(executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4"
                                                 "\\geckodriver-v0.30.0-win64\\geckodriver.exe")

# 1

chrome_driver.get('http://walla.co.il')
gecko_driver.get('http:/ynet.co.il')

# 2
# Walla site title compare
title_walla = 'וואלה! - האתר המוביל בישראל - עדכונים מסביב לשעון'
if chrome_driver.title == title_walla:
    print('Walla title matched')
else:
    print('Title not matched')

# Ynet site title compare
title_ynet = 'ynet - חדשות, כלכלה, ספורט ובריאות - דיווחים שוטפים מהארץ ומהעולם'
if gecko_driver.title == title_ynet:
    print('Ynet title matched')
else:
    print('Title not matched')

# 3

chrome_driver = webdriver.Chrome(
    executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4\\chromedriver_win32\\chromedriver.exe")
gecko_driver = webdriver.Firefox(
    executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4\\geckodriver-v0.30.0-win64"
                    "\\geckodriver.exe")

gecko_driver.get('http://ynet.co.il')
chrome_driver.get('http://ynet.co.il')

# Same xpath locators
chrome_driver.find_element_by_xpath('//*[@id="headerWeatherSelect"]/a').click()
gecko_driver.find_element_by_xpath('//*[@id="headerWeatherSelect"]/a').click()

# 4

chrome_driver.get('https://translate.google.com')
chrome_driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div['
                                    '2]/c-wiz[1]/span/span/div/textarea').send_keys("שלום")

# 5

chrome_driver = webdriver.Chrome(
    executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4\\chromedriver_win32\\chromedriver.exe")
chrome_driver.implicitly_wait(10)

chrome_driver.get('https://youtube.com')
chrome_driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div['
                                    '2]/ytd-searchbox/form/div/div[1]/input').send_keys('queen')
chrome_driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()

# 6
chrome_driver = webdriver.Chrome(
    executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4\\chromedriver_win32\\chromedriver.exe")
chrome_driver.implicitly_wait(10)

chrome_driver.get('https://translate.google.com')
chrome_driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]'
                                    '/div[2]/c-wiz[1]/span/span/div/textarea').send_keys("שלום")
chrome_driver.find_element_by_class_name("er8xn").send_keys('test')
chrome_driver.find_element_by_name("D5aOJc vJwDU").send_keys('test')

# 7
chrome_driver = webdriver.Chrome(
    executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4\\chromedriver_win32\\chromedriver.exe")
chrome_driver.implicitly_wait(10)

chrome_driver.get('http://facebook.com')
chrome_driver.find_element_by_xpath('//*[@id="email"]').send_keys('myemail@gmail.com')
chrome_driver.find_element_by_xpath('//*[@id="pass"]').send_keys('your_password')
chrome_driver.find_element_by_class_name('_6ltg').click()

chrome_driver.find_element_by_xpath('//*[@id="email"]').get_attribute('email')

# 8
chrome_driver = webdriver.Chrome(
    executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4\\chromedriver_win32\\chromedriver.exe")
chrome_driver.implicitly_wait(10)
chrome_driver.get('https://youtube.com')

# Print all cookies
print(chrome_driver.get_cookies())

# delete all Cookies
chrome_driver.delete_all_cookies()
print(chrome_driver.get_cookies())

# 10

chrome_driver = webdriver.Chrome(
    executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4\\chromedriver_win32\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
chrome_driver.implicitly_wait(10)
chrome_driver.get('https://youtube.com')
