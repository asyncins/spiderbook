import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as driver:
    # 访问指定网址
    driver.get("https://www.phei.com.cn/module/goods/wssd_index.jsp")
    # 定位版权信息
    footer = driver.find_element_by_class_name("web_book_footer")
    # 移动到指定位置
    ActionChains(driver).move_to_element(footer).perform()
    time.sleep(10)