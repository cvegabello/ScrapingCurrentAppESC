from dataBaseMySQLClass import DataBase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#import pandas as pd
import time
import pymysql
from pymysql import Error
from datetime import datetime


# definer pagina a scrapear y ruta donde descargaste chromediver
website = 'http://nypdcweb/escadmin/Login.do'
path = './chromedriver' #escribe tu ruta aqui

# definer variable 'driver'
driver = webdriver.Chrome(path)
# abrir Google Chrome mediante chromedriver
driver.get(website)
driver.maximize_window()

time.sleep(3)

userNameTx = driver.find_element_by_name("username")
userNameTx.send_keys("cvega")

passwordTx = driver.find_element_by_name("password")
passwordTx.send_keys("OpsrEsc")

signInBtn = driver.find_element_by_name("submit")
signInBtn.click()

time.sleep(3)

appMenu = driver.find_element_by_xpath('//*[@id="gtech-scroll-header"]/table/tbody/tr/td/div/ul/table/tbody/tr/td[4]/li/a')
appMenu.click()

currentAppMenu = driver.find_element_by_link_text ('Current Applications')
currentAppMenu.click()

driver.fullscreen_window()

appsNameList = driver.find_elements_by_xpath("//tbody/tr[@role='row']/td[2]")
appsVersionList = driver.find_elements_by_xpath("//tbody/tr[@role='row']/td[4]")
appsLastSubmitList = driver.find_elements_by_xpath("//tbody/tr[@role='row']/td[5]")

driver.close

appsNameListStr = []
for app in appsNameList:
    appsNameListStr.append(app.text)

appsLongVersionListStr = []
for app in appsVersionList:
    appsLongVersionListStr.append(app.text)


appsLastSubmitListStr = []
for app in appsLastSubmitList:
    fecha_dt = datetime.strptime(app.text, '%b %d, %Y %I:%M:%S %p')
    appsLastSubmitListStr.append(fecha_dt)

numElements = len(appsNameList)

appsShortVersionListStr = []
for i in range(numElements):
    posFirstInt = appsLongVersionListStr[i].find(":")
    posSegInt = appsLongVersionListStr[i].find(":", posFirstInt + 1)
    appsShortVersionListStr.append(appsLongVersionListStr[i][posSegInt + 1:])

driver.quit()

#Database
database = DataBase()
arg = []
database.execStoreProcNoRecords("deleteTerminalApp", arg)
# sqlStr = "DELETE FROM terminal_application"
# database.queryNoRecords(sqlStr)

for i in range(numElements):
    arg = [appsNameListStr[i], appsShortVersionListStr[i], appsLastSubmitListStr[i]]
    database.execStoreProcNoRecords("insert_terminal_app", arg)

    # sqlStr = "INSERT INTO boardinfony.terminal_application (application_name, version, update_datetime) VALUES ('{}', '{}', '{}')".format(appsNameListStr[i], appsShortVersionListStr[i], appsLastSubmitListStr[i])
    # database.queryNoRecords(sqlStr)

database.close()

# Create File Flag
with open("//10.5.165.84/SharedFolderBoard/flagFileAppVersion.txt", "w" , encoding="utf-8") as f:
    f.write(str(datetime.now) + ": Ready Version Terminal")
    f.close


# Pandas
# df = pd.DataFrame({'applications':applications})
# print(df)
#df.to_csv('apps.csv', index=False)

