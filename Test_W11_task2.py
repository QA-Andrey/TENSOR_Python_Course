from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://fix-online.sbis.ru/')
sleep(2)

login = driver.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled')
login.send_keys('mbappe_pk', Keys.ENTER)
sleep(2)

password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled')
password.send_keys('Демо123', Keys.ENTER)
sleep(20)

sleep(10)
accordeon_items = driver.find_elements(By.CSS_SELECTOR, '.NavigationPanels-Accordion__item')
accordeon_items[0].click()
sleep(10)

contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
contacts.click()
sleep(30)

new_message_btn = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
new_message_btn.click()
sleep(30)

adressee = driver.find_elements(By.CSS_SELECTOR, '.controls-Field')
adressee[0].send_keys('килиан')
sleep(2)

me = driver.find_element(By.CSS_SELECTOR, '[title = "Килиан_ПК Мбаппе"]')
me.click()
sleep(10)

text_box = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')
text_box.send_keys("Сообщение самому себе", Keys.CONTROL, Keys.ENTER)
sleep(5)

reestr = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-layout__text')
last_msg = reestr[0].text
assert last_msg == 'Сообщение самому себе', 'Сообщение не соответствует "Сообщение самому себе"'

action_chain = ActionChains(driver)
action_chain.context_click(reestr[0])
action_chain.perform()
sleep(5)

popup_menu_btns = driver.find_elements(By.CSS_SELECTOR, '[template="Controls/menu:Popup"] [data-qa=item]')
popup_menu_btns[6].click()
sleep(5)

delete_conf = driver.find_element(By.CSS_SELECTOR, '.controls-ConfirmationDialog__message-centered')
delete_conf.text == 'Диалог удален', "Нет подтверждения удаления диалога"

ok_btn = driver.find_element(By.CSS_SELECTOR, '[templatename="Controls/popupTemplate:ConfirmationDialog"] .controls-BaseButton__wrapper')
ok_btn.click()



