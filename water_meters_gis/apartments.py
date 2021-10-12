from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_conf import ELLIS_URL, chromedriver_path, TSZH, PASS_TSZH
from time import sleep
import xlsxwriter

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chromedriver_path, options=options)


def get_apart():
    driver.get(ELLIS_URL)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#orgcode"))).send_keys(TSZH)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(PASS_TSZH)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form p b input"))).click()
    sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Ведомости"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#vidotch"))).send_keys(Keys.DOWN)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#PrintOtchForm input"))).click()

    table = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#oborTable tbody tr")))

    wb = xlsxwriter.Workbook('apartments.xlsx')
    wsheet = wb.add_worksheet()
    wsheet.set_column('A:E', 10)
    bold = wb.add_format({'bold': True})
    wsheet.write_row('A1', ['№ кв', 'Площадь', 'Комнат', 'Проживают', 'Прописаны'], bold)
    wsheet.insert_image('F1', 'python-powered.png')
    nrow = 2
    for row in table:
        apart_num = row.find_element_by_xpath('./td[2]').text
        if apart_num:
            print(apart_num)
            area = float(row.find_element_by_xpath('./td[5]').text)
            reside = int(row.find_element_by_xpath('./td[3]').text)
            registered = int(row.find_element_by_xpath('./td[4]').text)
            rooms = 1
            if float(area) > 40:
                rooms = 2
            wsheet.write_row(f'A{nrow}', (apart_num, area, rooms, reside, registered))
            nrow += 1
    wb.close()
    return


get_apart()
