import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 计算账号数量，每两个参数为一组账号信息
acccounts = int(len(sys.argv[1:]) / 2)
print(f'Config {acccounts} accounts')

for i in range(acccounts):
    # 根据新的顺序，提取邮箱和密码
    email = sys.argv[1 + 2 * i]
    passwd = sys.argv[2 + 2 * i]
    print('----------------------------')

    # 1.打开浏览器
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 720)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i + 1} loading game...')
    sleep(20)

    # 2.输入邮箱
    screen = driver.find_element(By.ID, 'layaCanvas')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, -100)\
        .click()\
        .perform()
    driver.find_element(By.NAME, 'input').send_keys(email)
    print('Input email successfully')

    # 3.输入密码
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, -50)\
        .click()\
        .perform()
    driver.find_element(By.NAME, 'input_password').send_keys(passwd)
    print('Input password successfully')

    # 4.登录
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 250, 50)\
        .click()\
        .perform()
    print('Entering game...')
    sleep(20)  # 加载中...
    print('Login success')
    driver.quit()
