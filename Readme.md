# Atomy fast payment
![Alt text](image.png)
有了這個程式，搶貨再也不會輸別人 🐱🐱🐱

## 事先準備
- python 安裝
- 瀏覽器
- 瀏覽器 Driver (ChromeDriver、Microsoft Edge Driver等)

### python package installation
`pip install ...`
- selenium

## 介紹
### 邏輯
1. 在商品缺貨的情況下仍然可以進入到結帳頁面輸入資訊
2. 將事先打在 info.txt 上訂購資訊快速輸入，節省時間



### 使用
1. 新增 `info.txt` file，內容可以參考 info_example.txt

2. `python main.py` 執行程式

### 檔案說明
- main.py: 主程式
- utils.py: 其他邏輯函式

## 其他備註
### 開發目的
幫助有在使用艾多美官網上購物的家人

### 時間紀錄
- 2023/8/1: 完成基礎邏輯

### Todo
- [ ] 完善程式架構
- [ ] 時間判斷邏輯
- [ ] 打包成 .exe file

### 相關資源
- 瀏覽器必須使用最新版本的
    - [ChromeDriver 下載網站](https://chromedriver.chromium.org/)
    - [Edge Driver 下載網站](https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver/)
- Atomy 官網: https://www.atomy.com/tw/home

