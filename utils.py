import re

def openFile(fileName):
    file = open(fileName, 'r', encoding="utf-8")

    return file

def readInfoFromFile(file):
    info = []
    texts = file.readlines() # read the info line by line
    print(texts)

    for i in range(len(texts)):
        # personal info start with '---' (below)
        if re.match(r'^---', texts[i]):
            info = texts[i+1:]
            break
    info = [line.rstrip('\n') for line in info]
    print('info:', info)

    return info

def getAccountAndPassword(info):
    print('info:', info)
    accountNumber = info[0]
    password = info[1]
    return accountNumber, password

def getProductAndAmount(info):
    product = info[2]
    amount = info[3]
    return product, amount

def getSenderInfo(info):
    sCellPhone = info[4]
    sPhone = info[5]
    sEmail = info[6]
    sName = info[7]
    return sCellPhone, sPhone, sEmail, sName

def getReceiverInfo(info):
    rName = info[9]
    rCellPhone = info[11]
    rPhone = info[12]
    rAddress = info[13]
    return rName, rCellPhone, rPhone, rAddress

def getPaidMethod(info):
    paidMethod = info[14]
    return paidMethod