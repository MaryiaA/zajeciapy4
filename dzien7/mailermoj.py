import smtplib
import dzien7.secretsmoj

adresat = dzien7.secretsmoj.login
nadawca = dzien7.secretsmoj.login
haslo = dzien7.secretsmoj.haslo

mailer = smtplib.SMTP('smtp.gmail.com', 587)

mailer.ehlo()
mailer.starttls()
mailer.login(nadawca, haslo)


temat = 'Subject: Hello from Maryia'

wiadomosc = 'To jest moja wiadomosc'

tresc = temat + wiadomosc



mailer.sendmail(nadawca, adresat, tresc)
print("wyslano maila")
mailer.close()