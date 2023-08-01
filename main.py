from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import utils

ed = webdriver.Edge()
file = utils.openFile('info.txt')
info = utils.readInfoFromFile(file)
accountNumber, password = utils.getAccountAndPassword(info)
product, amount = utils.getProductAndAmount(info)

# 登入
ed.get('https://www.atomy.com/tw/Home/Account/Login')
ed.maximize_window()
userInput = ed.find_element(By.ID, "userId")
passwordInput = ed.find_element(By.ID, "userPw")
userInput.send_keys(accountNumber)
passwordInput.send_keys(password)
loginButton = ed.find_element(By.XPATH, '//*[@id="frm"]/div/div/div[1]/p[1]/a')
loginButton.click()
sleep(1)

# 直接進入商品購物頁面
url = f'https://www.atomy.com/tw/Home/Payment/OrderPayment?GdsCode={product}&Qty={amount}'
ed.get(url)
print(url)

# 填入預先輸入的資料
sCellPhone, sPhone, sEmail, sName = utils.getSenderInfo(info)
rName, rCellPhone, rPhone, rAddress = utils.getReceiverInfo(info)
ed.find_element(By.ID, 'tCellPhone').send_keys(sCellPhone)
ed.find_element(By.ID, 'tPhone1').send_keys(sPhone[0:4])
ed.find_element(By.ID, 'tPhone2').send_keys(sPhone[4:])
username, domain = sEmail.split('@')
ed.find_element(By.ID, 'tEmail1').send_keys(username)
ed.find_element(By.ID, 'tSendName').send_keys(sName)
ed.find_element(By.ID, 'tRevUserName').send_keys(rName)
ed.find_element(By.ID, 'tRevCellPhone').send_keys(rCellPhone)
ed.find_element(By.ID, 'tRevPhone1').send_keys(rPhone[0:4])
ed.find_element(By.ID, 'tRevPhone2').send_keys(rPhone[4:])
ed.find_element(By.ID, 'tRevAddr2').send_keys(rAddress)

# 選擇付款方式並打勾
if(utils.getPaidMethod(info).startswith("1")):
    ed.find_element(By.ID, 'settleGubun2').click()
    ed.find_element(By.ID, 'bAccountNo').click()
    ed.find_element(By.ID, 'tIpgumName').send_keys(sCellPhone)
elif(utils.getPaidMethod(info).startswith("2")):
    ed.find_element(By.ID, 'settleGubun3').click()
ed.find_element(By.ID, "chkAgree").click()

sleep(600)
ed.quit()


