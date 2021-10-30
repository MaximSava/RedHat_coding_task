from selenium import webdriver

chrome_driver = webdriver.Chrome(executable_path="C:\\Users\\MaxSa\\PycharmProjects\\DevOps-Course\\Lesson_4"
                                                 "\\chromedriver_win32\\chromedriver.exe")
chrome_driver.implicitly_wait(10)

chrome_driver.get('http://buyme.co.il')


def chrome_driver_setup(site, webdriver_path):
    chrome_driver = webdriver.Chrome('webdriver_path')
    chrome_driver.implicitly_wait(10)
    chrome_driver.get('site')


def site_manipulation(xpath, element):
    site_click = 'chrome_driver.find_element_by_xpath(' + '\'' + xpath + '\'' + ')' + '.' + element + '()'
    print(site_click)
    return exec(site_click)


# home screen xpath variables
amount, amount_100 = '//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2]', '//*[@id="ember1012_chosen"]'
area, area_merkaz = '//*[@id="ember1027_chosen"]/a/span', '//*[@id="ember1027_chosen"]/div/ul/li[3]'
category, category_local_voucher = '//*[@id="ember1037_chosen"]/a/span', '//*[@id="ember1037_chosen"]/div/ul/li[2]'
search_voucher_button = '//*[@id="ember1072"]'

# Registration xpath variables
reg_button, reg_link = '//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2]', '//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span'
reg_name = '//*[@id="ember1482"]'
reg_mail = '//*[@id="ember1485"]'
reg_pass = '//*[@id="valPass"]'
reg_pass_confirm = '//*[@id="ember1491"]'
reg_complete_button = '//*[@id="ember1493"]/span'


# Login x path variables


# Choose bussiness screen variables
bussiness_choose = '//*[@id="ember1747"]/div[2]/span'
vaucher_amount_for_bussiness = '//*[@id="ember1778"]'
vaucher_bussiness_click_button = '//*[@id="ember1780"]'
vaucher_reciver_name = '//*[@id="ember1883"]'
vaucher_text_area = '//*[@id="ember1890"]/textarea'
vaucher_add_picture = 'ember1899'


# הרשמה

chrome_driver.find_element_by_xpath('//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2]').click()
chrome_driver.find_element_by_xpath('//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span').click()
chrome_driver.find_element_by_xpath('//*[@id="ember1482"]').send_keys('מקסים')
chrome_driver.find_element_by_xpath('//*[@id="ember1485"]').send_keys('buymetest@mailgw.com')
chrome_driver.find_element_by_xpath('//*[@id="valPass"]').send_keys('Mypass11')
chrome_driver.find_element_by_xpath('//*[@id="ember1491"]').send_keys('Mypass11')
chrome_driver.find_element_by_xpath('//*[@id="ember1493"]/span').click()

# Login

# Home screen site
chrome_driver.find_element_by_xpath('//*[@id="ember1012_chosen"]').click()
chrome_driver.find_element_by_xpath('//*[@id="ember1012_chosen"]/div/ul/li[2]').click()

chrome_driver.find_element_by_xpath('//*[@id="ember1027_chosen"]/a/span').click()
chrome_driver.find_element_by_xpath('//*[@id="ember1027_chosen"]/div/ul/li[3]').click()

chrome_driver.find_element_by_xpath('//*[@id="ember1037_chosen"]/a/span').click()
chrome_driver.find_element_by_xpath('//*[@id="ember1037_chosen"]/div/ul/li[2]').click()

chrome_driver.find_element_by_xpath('//*[@id="ember1072"]').click()

# Choose bussiness screen
chrome_driver.find_element_by_xpath('//*[@id="ember1747"]/div[2]/span').click()
chrome_driver.find_element_by_xpath('//*[@id="ember1778"]').send_keys('100')
chrome_driver.find_element_by_xpath('//*[@id="ember1780"]').click()
chrome_driver.find_element_by_xpath('//*[@id="ember1883"]').send_keys('נטלי')
chrome_driver.find_element_by_xpath('//*[@id="ember1890"]/textarea').send_keys('פינוק ממני')
chrome_driver.find_element_by_id('ember1899').send_keys('C:\\Users\\MaxSa\\Desktop\\world of games\\doll_2.png')
# chrome_driver.find_element_by_xpath('//*[@id="ember1936"]').click()
