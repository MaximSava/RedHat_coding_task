"""
Buyme site home screen,choose bussiness,sender reciver screen test

"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CHROME_WEBDRIVER_PATH = 'C:/Users/MaxSa/PycharmProjects/DevOps-Course/' \
                        'Lesson_4/chromedriver_win32/chromedriver.exe'

# Path to profile picture
PATH_TO_PICTURE_FILE = 'C:/Users/MaxSa/Desktop/world_of_games/doll_2.png'

# Email for registration
REG_EMAIL = 'buymetest3@mailgw.com'

#  Configuration for driver
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
chrome_driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH, options=chrome_options)

chrome_driver.get('http://buyme.co.il')

# home screen xpath variables
home_screen_list = {
    'amount': '//*[@id="ember1012_chosen"]/a/span.click()',
    'amount_100': '//*[@id="ember1012_chosen"]/div/ul/li[2].click()',
    'area': '//*[@id="ember1027_chosen"]/a/span.click()',
    'area_merkaz': '//*[@id="ember1027_chosen"]/div/ul/li[3].click()',
    'category': '//*[@id="ember1037_chosen"]/a/span.click()',
    'category_local_voucher': '//*[@id="ember1037_chosen"]/div/ul/li[2].click()',
    'search_voucher_button': '//*[@id="ember1072"].click()'

}

# Choose bussiness screen variables
choose_bussiness_list = {
    'bussiness_choose_button': '//div[@class="bottom"].click()',
    'vaucher_amount_for_bussiness': '//input[@placeholder="הכנס סכום"].send_keys("100")',
    'vaucher_bussiness_click_button': '//button[@gtm="בחירה"].click()',
    'vaucher_reciver_name': '//input[@data-parsley-required-message='
                            '"מי הזוכה המאושר? יש להשלים את שם המקבל/ת"].send_keys("נטלי")',
    'vaucher_text_area': '//textarea[@data-parsley-group="voucher-greeting"].send_keys("פינוק ממני")',
    'vaucher_continue_button': '//button[@gtm="המשך"].click()',
    'vaucher_circle_area_click': '//div[@class="circle-area"].click()',
    'vaucher_sms_telephone': '//*[@id="sms"].send_keys("0526180349")',
    'vaucher_sms_sender': '//input[@placeholder="מספר נייד"].send_keys("0526180349")',
    'vaucher_sender_name': '//input[@placeholder="שם שולח המתנה"].send_keys("מקסים")',
    'vaucher_continiue_button': '//button[starts-with(@gtm,"המשך")].click()'
}

def site_cliker(site_xpath_list: dict):
    # send data to bussiness choose list
    for i in site_xpath_list:
        slice_start_xpath = site_xpath_list[i][:].split('.')
        slice_start_xpath = slice_start_xpath[0]
        print(slice_start_xpath)
        men_menu = WebDriverWait(chrome_driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, slice_start_xpath)))
        if 'click' in site_xpath_list[i]:
            print(slice_start_xpath)
            men_menu.click()

        elif 'send_keys' in site_xpath_list[i]:

            if 'C:/' in site_xpath_list[i]:
                men_menu = WebDriverWait(chrome_driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, '//input[@name="logo"]')))
                men_menu.send_keys(PATH_TO_PICTURE_FILE)

            elif 'מייל' in site_xpath_list[i]:

                men_menu.send_keys(REG_EMAIL)

            else:
                send_key_value = site_xpath_list[i].split(".")
                send_key_value = send_key_value[1].strip('send_keys()\"\"')
                print(slice_start_xpath)
                print(send_key_value)
                men_menu.send_keys(send_key_value)


if __name__ == "__main__":
    site_cliker(home_screen_list)
    site_cliker(choose_bussiness_list)
    print('Test Passed')
    chrome_driver.close()

