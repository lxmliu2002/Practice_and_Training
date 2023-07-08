from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from tqdm import tqdm

def is_element_exist(): 
    try:
        driver.find_element(By.XPATH,'//li/div/div/a/img')
        return True
    except:
        return False


service = Service("F:\Venvs\week2\Scripts\msedgedriver.exe")
options = webdriver.EdgeOptions()
# options.add_argument("headless")
driver = webdriver.Edge(service=service,options=options)
data = pd.read_csv('.\data\star_infos_new.csv')
imgs = []
for name in tqdm(data['name'],total=len(data['name']), desc='Searching'):
    b_str = name.encode()
    a_str = ''
    for  i in range(len(b_str)):
        a_str += str(hex(b_str[i])).replace('0x','%').upper()
    print(a_str)

    url = "https://image.baidu.com/search/index?tn=baiduimage&word=" + a_str

    print(url)

    driver.get(url=url)
    while not is_element_exist():
        driver.refresh()
        time.sleep(0.1)
    content = driver.find_element(By.XPATH,'//li/div/div/a/img')
    text = content.get_attribute('data-imgurl')
    print(text)
    imgs.append(text)
data['image'] = imgs
data.to_csv('.\data\star_infos_new2.csv',index=False)