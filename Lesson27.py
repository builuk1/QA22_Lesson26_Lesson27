# from selenium import webdriver
# import time
#
# url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(url)
# # ANSWERS
# answer_1 = 'M'
# answer_2 = 'A'
# answer_9 = 'b'
# answers_19 = 'adadadadad'
# # XPATH
# xpath_entry_1 = '//input[@name="q1"]'
# xpath_entry_2 = '//input[@name="q2"]'
# xpath_radio_9 = f'//input[@name="q9"][@value="{answer_9}"]'
#
#
# # Questions
# entry_1 = driver.find_element('xpath', xpath_entry_1)
# entry_1.send_keys(answer_1)
#
# entry_2 = driver.find_element('xpath', xpath_entry_2)
# entry_2.send_keys(answer_2)
#
# radio_9 = driver.find_element('xpath', xpath_radio_9)
# radio_9.click()
#
# for checkbox_19 in answers_19:
#     xpath_checkbox_19 = f'//input[@name="q19"][@value="{checkbox_19}"]'
#     checkbox_19 = driver.find_element('xpath', xpath_checkbox_19)
#     checkbox_19.click()


from selenium import webdriver
import time

url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# ANSWERS
with open('answers.txt', 'rt') as f:
    answer_1 = f.readline()[:-1]
    answer_2 = f.readline()[:-1]
    answer_9 = f.readline()[:-1]
    answers_19 = f.readline()[:-1]
# XPATH
xpath_entry_1 = '//input[@name="q1"]'
xpath_entry_2 = '//input[@name="q2"]'
xpath_radio_9 = f'//input[@name="q9"][@value="{answer_9}"]'

xpath_button_finish = '//input[@value="FINISHED"]'
xpath_textarea_result = '//textarea[@id="Result"]'
# Questions
entry_1 = driver.find_element('xpath', xpath_entry_1)
entry_1.send_keys(answer_1)

entry_2 = driver.find_element('xpath', xpath_entry_2)
entry_2.send_keys(answer_2)

radio_9 = driver.find_element('xpath', xpath_radio_9)
radio_9.click()

for checkbox_19 in answers_19:
    xpath_checkbox_19 = f'//input[@name="q19"][@value="{checkbox_19}"]'
    checkbox_19 = driver.find_element('xpath', xpath_checkbox_19)
    checkbox_19.click()

#Кликнуть на финиш, чтобы скачать результат
button_finish = driver.find_element('xpath', xpath_button_finish)
button_finish.click()

#Не рабочий вывод результата
# textarea_result = driver.find_element('xpath', xpath_textarea_result)
# print(textarea_result.text)

#Вывод результата
print(driver.execute_script("return document.IQtest.Result.value"))