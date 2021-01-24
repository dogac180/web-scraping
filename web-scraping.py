import time
import requests
import os
import pandas as pd
from selenium import webdriver
import pdb

driver = webdriver.Chrome(executable_path=r'/Users/Elma/Desktop/chromedriver')
directory = r"/Users/Elma/Desktop/LASTİTEMS"
data = pd.read_excel(r'/Users/Elma/Desktop/LEFTOVERSFROMSCRAPİNG.xlsx')
df = pd.DataFrame(data, columns= ['ÜRÜN ADI'])
items_list = df.to_numpy()

def save_img(product, url, i):
    try:
        filename = product + str(i) + '.jpg'
        response = requests.get(url)
        if response.ok:
            image_path = os.path.join(directory, filename)
            file = open(image_path, "wb")
            file.write(response.content)
            file.close()
        else:
            pass

    except Exception as e:
        print(e)

def find_urls(product, url, driver):
    driver.get(url)
    time.sleep(3)
    for j in range(1, 2):
        try:
            imgurl = driver.find_element_by_xpath(
                '//div//div//div//div//div//div//div//div//div//div[' + str(j) + ']//a[1]//div[1]//img[1]')
            imgurl.click()
        except Exception as e:
            print(e)
        time.sleep(8)
        try:
            img = driver.find_element_by_xpath(
                '//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute(
                "src")
            save_img(product, img, j)
        except Exception as e:
            print("Image for product ", product, "can not be found.")

for product in items_list:
    url = 'https://www.google.com/search?q=' + product[0] + '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'
    driver.get(url)
    find_urls(product[0], url, driver)
