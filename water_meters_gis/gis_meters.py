from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from my_conf import ELLIS_URL, chromedriver_path, TSZH, PASS_TSZH, GIS_URL, SNILS, PASS_GIS
from time import sleep
import csv
import os

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chromedriver_path, options=options)


def get_meters():
    driver.get(ELLIS_URL)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/section/div[2]/article/div/strong/div[6]/div[1]/'
                                 'div/div/form/input[1]').send_keys(TSZH)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/section/div[2]/article/div/strong/div[6]/div[1]/'
                                 'div/div/form/input[2]').send_keys(PASS_TSZH)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/section/div[2]/article/div/strong/div[6]/div[1]/'
                                 'div/div/form/p/b/input').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/section/div[2]/article/div/strong/div[6]/ul/'
                                 'li[6]/a').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/button').click()
    sleep(1)
    table = driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div/div/div/section/div[2]/article/div/strong/'
                                          'div[6]/div[6]/div[4]/div[1]/div/table/tbody/tr')
    sleep(1)
    csv_header = ['apartment', 'cw_meter', 'hw_meter']
    with open('meters.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        for row in table:
            apart = row.find_element_by_class_name('KV').text
            if apart[-1] == 'А':
                apart = apart[:-1]
            elif apart[-1] == 'Б':
                continue
            cw_meter = row.find_element_by_class_name('XVNOCOUNT').text
            hw_meter = row.find_element_by_class_name('GVNOCOUNT').text
            writer.writerow([apart, cw_meter, hw_meter])


if not os.path.exists('meters.csv'):
    get_meters()
if os.stat('meters.csv').st_size == 0:
    get_meters()
with open('meters.csv', 'r') as f:
    reader = csv.reader(f)
    ellis_meters = {row[0]: (row[1], row[2]) for row in reader}

driver.get(GIS_URL)

# authorization
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "signed-status-badge a"))).click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login"))).send_keys(SNILS)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(PASS_GIS)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginByPwdButton"))).click()
# choose legal
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#org0"))).click()
# security alert
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#saveCookie"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bContinue"))).click()
# info msg
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-base__close"))).click()
# choose meters page
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Объекты управления"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Приборы учета"))).click()
# choose location
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[7]/div/div/div[1]/"
            "ef-hcs-pu-bppu/ef-bp-form/div/form/div[2]/div/div/form/fieldset/accordion/div/div[2]/div[1]/a"))).click()

# choose street entry
sleep(1)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#s2id_streetpa3 a"))).click()
# enter street
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#select2-drop input"))).send_keys('Новосмоленская')
# confirm street option
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop ul div"))).click()
# choose bld entry
sleep(2)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#s2id_autogen93 a'))).click()
# enter a number
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#select2-drop input"))).send_keys('2 Литер А')
# confirm bld option
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop ul div"))).click()

for apart, meters in ellis_meters.items():
    if apart == 'apartment':
        continue
    print(f'{apart} Start')
    # choose apartment entry
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div/div/div[1]/ef-hcs-pu-bppu/ef-bp-form/div/form/div[2]/div/div/form/fieldset/accordion/div/div[2]/div[2]/ef-pa-form-4/div/form/div/div/div/div[2]/div[12]/div/div[1]/div/div/a'))).click()
    except ElementClickInterceptedException:
        print('Intercepted')
        sleep(10)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div/div/div[1]/ef-hcs-pu-bppu/ef-bp-form/div/form/div[2]/div/div/form/fieldset/accordion/div/div[2]/div[2]/ef-pa-form-4/div/form/div/div/div/div[2]/div[12]/div/div[1]/div/div/a'))).click()
    # enter a number
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#select2-drop input"))).send_keys(apart)
    # confirm apartment option
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop ul div"))).click()
    except ElementClickInterceptedException:
        print('Intercepted')
        sleep(3)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop ul div"))).click()
    print(f'Apart: {apart} OK')
    # find
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[7]/div/div/div[1]/ef-hcs-pu-bppu/ef-bp-form/div/form/div[3]/div/div[2]/button"))).click()
    print('Find OK')
    sleep(3)


    def get_from_gis():
        try:
            # meters_gis = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[7]/div/div/div[3]/div/ef-hcs-pu-sppu/div/ng-simple-grid/div/div[1]/table/tbody/tr")))
            meters_gis = driver.find_elements_by_xpath(
                '/html/body/div[1]/div[7]/div/div/div[3]/div/ef-hcs-pu-sppu/div/'
                'ng-simple-grid/div/div[1]/table/tbody/tr')
            print('Meters OK')
        except ElementClickInterceptedException:
            sleep(2)
            print('Interception')
            meters_gis = driver.find_elements_by_xpath(
                '/html/body/div[1]/div[7]/div/div/div[3]/div/ef-hcs-pu-sppu/div/'
                'ng-simple-grid/div/div[1]/table/tbody/tr')
        except:
            print('No items')
            meters_gis = []
        # print(meters_gis)
        gis_meters = []
        if meters_gis and meters_gis[0]:
            sleep(0.3)
            # for m in meters_gis:
            #     sleep(0.1)
            #     mnum = m.find_element_by_css_selector('td').text
            #     sleep(0.1)
            #     gis_meters.append(mnum)
            try:
                gis_meters = [m.find_element_by_css_selector('td').text for m in meters_gis]
            except StaleElementReferenceException:
                sleep(2)
                print('Stale exception')
                meters_gis = driver.find_elements_by_xpath('/html/body/div[1]/div[7]/div/div/div[3]/div/ef-hcs-pu-sppu/div/'
                                                           'ng-simple-grid/div/div[1]/table/tbody/tr')
                sleep(2)
                gis_meters = [m.find_element_by_css_selector('td').text for m in meters_gis]
        else:
            gis_meters = []
        return gis_meters

    gis_meters = get_from_gis()
    if gis_meters and gis_meters[0] == '':
        sleep(2)
        gis_meters = get_from_gis()

    ellis_cwm = f'ХВ {meters[0]}'
    ellis_hwm = f'ГВ {meters[1]}'
    print(apart, gis_meters, meters)

    with open('recap.txt', 'a') as f:
        if ellis_cwm in gis_meters:
            f.write(f'Apart: {apart}. CWM: {ellis_cwm} OK!\n')
            gis_meters.remove(ellis_cwm)
        else:
            f.write(f'Apart: {apart}. There is no CWM {ellis_cwm}. Warning!\n')
        if ellis_hwm in gis_meters:
            f.write(f'Apart: {apart}. HWM: {ellis_hwm} OK!\n')
            gis_meters.remove(ellis_hwm)
        else:
            f.write(f'Apart: {apart}. There is no HWM {ellis_hwm}. Warning!\n')
        if gis_meters:
            f.write(f'Apart: {apart}. Meters {gis_meters} should be archived. Warning!\n')
    print('Writed!\n')
    meters_gis = None
    gis_meters = None
