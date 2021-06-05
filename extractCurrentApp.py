from selenium import webdriver
from selenium.webdriver.support.ui import Select
#import pandas as pd
import time
import pymysql
# import mysql.connector
from pymysql import Error


# # definer pagina a scrapear y ruta donde descargaste chromediver
# website = 'http://nypdcweb/escadmin/Login.do'
# path = 'C:/Users/cvegabello/Documents/VisualStudio2008/Projects/scrapingCurrentAppESC/chromedriver' #escribe tu ruta aqui

# # definer variable 'driver'
# driver = webdriver.Chrome(path)
# # abrir Google Chrome mediante chromedriver
# driver.get(website)
# driver.maximize_window()
# #driver.fullscreen_window()

# time.sleep(3)

# userNameTx = driver.find_element_by_name("username")
# userNameTx.send_keys("cvega")

# passwordTx = driver.find_element_by_name("password")
# passwordTx.send_keys("OpsrEsc")

# signInBtn = driver.find_element_by_name("submit")
# signInBtn.click()

# time.sleep(3)

# appMenu = driver.find_element_by_xpath('//*[@id="gtech-scroll-header"]/table/tbody/tr/td/div/ul/table/tbody/tr/td[4]/li/a')
# appMenu.click()

# currentAppMenu = driver.find_element_by_link_text ('Current Applications')
# currentAppMenu.click()

# driver.fullscreen_window()
# # appsList = driver.find_elements_by_xpath("//tbody/tr[@role='row']")

# #appsNameList = driver.find_elements_by_tag_name("u")
# appsNameList = driver.find_elements_by_xpath("//tbody/tr[@role='row']/td[2]")
# appsVersionList = driver.find_elements_by_xpath("//tbody/tr[@role='row']/td[4]")
# appsLastSubmitList = driver.find_elements_by_xpath("//tbody/tr[@role='row']/td[5]")


# driver.close

# appsNameListStr = []
# for app in appsNameList:
#     appsNameListStr.append(app.text)

# # for element in appsNameListStr:
# #     print(element)

# appsLongVersionListStr = []
# for app in appsVersionList:
#     appsLongVersionListStr.append(app.text)

# # for element in appsLongVersionListStr:
# #     print(element)

# appsLastSubmitListStr = []
# for app in appsLastSubmitList:
#     appsLastSubmitListStr.append(app.text)

# # for element in appsLastSubmitListStr:
# #     print(element)

# numElements = len(appsNameList)
# # for i in range(numElements):
# #     print(appsNameListStr[i] + "|" + appsLongVersionListStr[i] + "|" + appsLastSubmitListStr[i] )

# appsShortVersionListStr = []
# for i in range(numElements):
#     posFirstInt = appsLongVersionListStr[i].find(":")
#     posSegInt = appsLongVersionListStr[i].find(":", posFirstInt + 1)
#     appsShortVersionListStr.append(appsLongVersionListStr[i][posSegInt + 1:])

# # for element in appsShortVersionListStr:
# #     print(element)   

# for i in range(numElements):
#     print(appsNameListStr[i] + "|" + appsShortVersionListStr[i] + "|" + appsLastSubmitListStr[i] )

#Database
#host = '10.5.165.52',
try:
    connection = pymysql.connect(
        host = '10.5.165.52',
        port = 3306,
        user= 'opsNY',
        password= '',
        db= 'boardinfony'
    )
    print("connection successful")
except Error as ex:
    print("Connection error:", ex)


# Pandas
# df = pd.DataFrame({'applications':applications})
# print(df)
#df.to_csv('apps.csv', index=False)

