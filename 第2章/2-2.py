from selenium import webdriver

with webdriver.Chrome() as driver:
    # 访问指定网址
    driver.get("https://www.phei.com.cn/module/goods/wssd_index.jsp")
    # 定位图书列表
    lis = driver.find_elements_by_css_selector("#book_sort_area > ul:nth-child(1) > li")
    # 循环图书列表并从中提取图书信息
    for i in lis:
        image = i.find_element_by_css_selector("p > a > img").get_attribute("src")
        book = i.find_element_by_css_selector("p.li_title > a").text
        author = i.find_element_by_css_selector("p.li_author").text.split("\n")[0]
        price = i.find_element_by_css_selector("p.li_author > i").text
        print([book, price, author, image])