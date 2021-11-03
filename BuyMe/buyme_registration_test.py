"""
Buyme registration screen test
"""

import buyme_test

# Registration
registration_list = {
    'reg_button1': '//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2].click()',
    'reg_button2': '//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span.click()',
    'reg_name': '//input[@placeholder="שם פרטי"].send_keys("מקסים")',
    'reg_email': '//input[@placeholder="מייל"].send_keys("buymetest@mailgw.com")',
    'reg_pass': '//input[@placeholder="סיסמה"].send_keys("Mypass11")',
    'reg_pass_validate': '//input[@placeholder="אימות סיסמה"].send_keys("Mypass11")',
    'reg_send_button': '//button[@gtm="הרשמה ל-BUYME"].click()'
}

if __name__ == "__main__":
    buyme_test.site_cliker(registration_list)
    chrome_driver.close()
    print("Test Passed")
