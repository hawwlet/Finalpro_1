import smtplib
smtplibObj = smtplib.SMTP("smtp.gmail.com",587)
smtplibObj.ehlo()
smtplibObj.starttls()
smtplibObj.login("rizaldani07@gmail.com",)
smtplibObj.sendmail("rizaldani07@gmail.com",
                    "hari.rofalon.geous@gmail.com","Subject: Terima Kasih mas Hari atas ilmu nya")
smtplibObj.quit()