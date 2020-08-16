from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from maildeneme import mail
from hesap_control import kullaniciadi, sifre

class enabiz:
    def __init__(self, kullaniciadi, sifre):
        self.driver = webdriver.Firefox()
        self.driver.get("https://enabiz.gov.tr")
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre


    def login(self):
        username = self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys(self.kullaniciadi)
        password = self.driver.find_element_by_xpath('//*[@id="Sifre"]')
        password.send_keys(self.sifre)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="btnGiris"]').click()
        time.sleep(2)
        self.driver.get("https://enabiz.gov.tr/HastaBilgileri/Tahliller#Covid19Sonuc")
        
        try:
            elem = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/p')
            if "do" in elem.text:
                print("Sonuç açıklanmamış")
            else:
                print("Sonuç açıklandı.")
        except:
            self.driver.find_element_by_xpath('//*[@id="Covid19TahlilTable"]')
            mail.send_mail(self)
            print("Mail atıldı.")
            
                
while True:
        
    nabiz = enabiz(kullaniciadi, sifre)
    nabiz.login()
    time.sleep(1800)

