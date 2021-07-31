# from pandas.io.formats import style
from dataBaseMySQLClass import DataBase
from registerWindowsClass import WinRegistry
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from datetime import datetime
from datetime import date
import emailFuctions
from pretty_html_table import build_table



# definer pagina a scrapear y ruta donde descargaste chromediver
website = 'http://nypdcweb/escadmin/Login.do'
# path = 'C:/Users/cvegabello/Documents/VisualStudio2008/Projects/scrapingCurrentAppESC/chromedriver'
path = './chromedriver' #escribe tu ruta aqui

# print(path) 
# time.sleep(5)
# definer variable 'driver'
driver = webdriver.Chrome(path)
# driver = webdriver.Chrome(ChromeDriverManager(version="92.0.4515.107").install())
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

app_name = []
version = []
last_submit = []

for i in range(numElements):
    arg = [appsNameListStr[i], appsShortVersionListStr[i], appsLastSubmitListStr[i]]
    database.execStoreProcNoRecords("insert_terminal_app", arg)
    app_name.append(appsNameListStr[i])
    version.append(appsShortVersionListStr[i])
    last_submit.append(appsLastSubmitListStr[i])


    # sqlStr = "INSERT INTO boardinfony.terminal_application (application_name, version, update_datetime) VALUES ('{}', '{}', '{}')".format(appsNameListStr[i], appsShortVersionListStr[i], appsLastSubmitListStr[i])
    # database.queryNoRecords(sqlStr)

database.close()

#Read Registry windows
registry = WinRegistry()
pathStr = registry.readRegistry("InfoBoard", 0)

# Create File Flag
with open(pathStr + "/flagFileAppVersion.txt", "w" , encoding="utf-8") as f:
# with open("//10.5.165.84/SharedFolderBoard/flagFileAppVersion.txt", "w" , encoding="utf-8") as f:
    f.write("Ready Version Terminal")
    f.close


# Pandas
df = pd.DataFrame({'Application Name': app_name, 'Version': version, 'Last Submission Date': last_submit })
df_order_by_date = df.sort_values("Last Submission Date",ascending=False)
# print(df_order_by_date)

#Pretty table
html_table_blue_light = build_table(df_order_by_date, 'blue_light', font_size='13px', text_align='', width='150px')
with open('pretty_table.html', 'w') as f:
    f.write(html_table_blue_light)

#Send the email with the pretty table
today = date.today()
date_now_dt= today.strftime("%m/%d/%Y")
emailFuctions.send_email_bodyHtml("156.24.14.132","do.not.reply@igt-noreply.com","carlos.vegabello@igt.com, #NYOPS@IGT.com","Current Applications '{}'".format(date_now_dt), html_table_blue_light, [])
# emailFuctions.send_email_bodyHtml("156.24.14.132","do.not.reply@igt-noreply.com","carlos.vegabello@igt.com","Current Applications '{}'".format(date_now_dt), html_table_blue_light, [])