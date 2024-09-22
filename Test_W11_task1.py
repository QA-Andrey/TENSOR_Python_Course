from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://sbis.ru/')

contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu')
contacts_btn.click()
sleep(2)

contacts_btn_more = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon')
contacts_btn_more.click()
sleep(2)

tensor_banner = driver.find_element(By.CSS_SELECTOR, '[src="/static/resources/SabyRuPages/_contacts/images/logo.svg?x_module=b079a5ec5a820cde5be2af85e81ecfc0"]')
tensor_banner.click()
sleep(2)

driver.switch_to.window(driver.window_handles[1])
sleep(2)

power_in_people_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
assert power_in_people_block.is_displayed(), 'Блок "Сила в людях" не отображается'
power_in_people_text = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-Index__card-title')
assert power_in_people_text.text == "Сила в людях", 'Название блока отличается от "Сила в людях"'


power_in_people_block_about = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__link')
power_in_people_block_about.location_once_scrolled_into_view
power_in_people_block_about.click()
sleep(2)
assert driver.current_url == 'https://tensor.ru/about'
