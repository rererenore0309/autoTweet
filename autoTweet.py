from selenium import webdriver
from time import sleep
import datetime

#ブラウザ読み込み
driver = webdriver.Chrome()
print(driver)

#URLにアクセス
driver.get('https://twitter.com/login?lang=ja')
print('https://twitter.com/login?lang=ja')

#メールアドレス、パスワード入力する。
id = driver.find_element_by_class_name("js-username-field")
print(id)
id.send_keys('yourID')
password= driver.find_element_by_class_name("js-password-field")
password.send_keys('yourPassword')
sleep(1)
#ログイン
password.submit()
sleep(1)

#ツイート
tweet = driver.find_element_by_id('tweet-box-home-timeline')
#現在時刻を入力。
tweet.send_keys(str(datetime.datetime.now()))
sleep(1)
tweet_button = driver.find_element_by_class_name("tweet-action")
tweet_button.click()
sleep(1)

#ブラウザを閉じる
driver.close()
print('finish')
