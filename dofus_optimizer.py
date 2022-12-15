from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Stat Classes
HP_CLASS = 'css-b8t54k'

# Access classes
MAIN_CLASS = 'css-jp7wuz'
TABLE_CLASS = 'css-1cr5adz'

# Selection Classes
BASE_URL = 'https://dofuslab.io'
HELMET_URL = '/equip/e816a293-7e59-4ad5-900e-45b67fe30e38/'

def main():
    driver = webdriver.Chrome('/Users/rogebrd/Downloads/chromedriver')
    driver.get("https://dofuslab.io")
    current_hp = get_stat(driver, HP_CLASS)
    print(current_hp)
    select_item(driver, 0)
    new_hp = get_stat(driver, HP_CLASS)
    print(new_hp)


def select_item(driver, index):
    driver.get("{}{}".format(BASE_URL, HELMET_URL))

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, TABLE_CLASS))
    )
    table_entries = table.find_elements(By.TAG_NAME, 'div')
    
    item_to_select = table_entries[index]
    item_to_select.click()


def get_stat(driver, stat_class):
    
    stat_div = driver.find_element(By.CLASS_NAME, stat_class)
    stat_span = stat_div.find_element(By.TAG_NAME, 'span')
    stat = stat_span.text
    return stat


if __name__ == "__main__":
    main()