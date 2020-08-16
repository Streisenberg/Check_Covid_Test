import smtplib
from mail_control import alici,gonderen

class mail:
    def __init__(self, alici, gonderen):
        self.gonderen = gonderen
        self.alici = alici
        
    def send_mail(self):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        

        self.server.login(self.gonderen, "2FPassword")

        subject = "Covid Testi"
        body = "Sonuçları kontrol et"
        msg = f"Subject: {subject}\n\n{body}"
        msg = msg.encode("UTF-8")
        self.server.sendmail(self.gonderen,self.alici, msg)
        print("Email gönderildi")
        self.server.quit()
            
mail(alici,gonderen)
