from pytesseract import image_to_string
import pytesseract
import requests as rq
import os
import pdb
from selenium import webdriver
from PIL import Image as PImage
from selenium.webdriver.support.select import Select
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

parent_dir = 'D:/'
directory = 'autofill_images'
dirr = os.path.join(parent_dir, directory)
os.mkdir(dirr)
user_name = 'C0207202012825'
password = 'BaQmh'
url = 'https://eworkme.com/'
driver = webdriver.Chrome('/webdriver/chromedriver')
try:
    res = driver.get(url)
except:
    print('failed to load please check internet connection or the url, if it is correct?')
driver.find_element_by_xpath('//div[@class="form23132"]//input[@name="txt_Uname"]').send_keys(user_name)
driver.find_element_by_xpath('//div[@class="form23132"]//input[@name="txt_pass"]').send_keys(password)
driver.find_element_by_xpath('//input[@type="submit"]').click()
select_fr = Select(driver.find_element_by_name("ctl00$ContentPlaceHolder1$drp_pagejump"))
select_fr.select_by_value('705')
for i in range(1,2):
    img = driver.find_element_by_xpath('//div[@class="control-group"]//img')
    src = img.get_attribute('src')
    print('333333333333333333333333333')
    print(src)
    img_data = rq.get(src).content
    with open('D:/autofill_images/'+str(i)+'.jpg', 'wb+') as f:
        f.write(img_data)
        f.close()
        print(f)
    img = PImage.open('D:/autofill_images/' + '{}.jpg'.format(i))
    text = image_to_string(img)
    print(text)
    list = text.split('\n')
    print(list)
    uniq_id = list[0].replace(" ",'')
    full_name = list[1]
    contact_details = list[2]
    salary = list[3]
    address = list[4]
    driver.find_element_by_xpath('//div[@class="input-with-icon  right"]//input[@name="ctl00$ContentPlaceHolder1$txt_tbc"]').send_keys(uniq_id)
    driver.find_element_by_xpath('//div[@class="input-with-icon  right"]//input[@name="ctl00$ContentPlaceHolder1$txt_name"]').send_keys(full_name)
    driver.find_element_by_xpath('//div[@class="input-with-icon  right"]//input[@name="ctl00$ContentPlaceHolder1$txt_mobno"]').send_keys(contact_details)
    driver.find_element_by_xpath('//div[@class="input-with-icon  right"]//input[@name="ctl00$ContentPlaceHolder1$txt_licenceno"]').send_keys(salary)
    driver.find_element_by_xpath('//div[@class="input-with-icon  right"]//input[@name="ctl00$ContentPlaceHolder1$txt_Hadd"]').send_keys(address)
    pdb.set_trace()
    driver.find_element_by_xpath('//input[@name="ctl00$ContentPlaceHolder1$btnsubmit"]').click()
