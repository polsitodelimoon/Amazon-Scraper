import smtplib, ssl
import pandas as pd
from time import sleep
import os
from datos import FOR, TO, PASSWORD

archivo1 = pd.read_csv('search.csv')
archivo2 = pd.read_csv('search.csv')

link1 = archivo1['product url'].tolist()
link2 = archivo2['product url'].tolist()
precio1 = archivo1['price'].tolist()
precio2 = archivo2['price'].tolist()

smtp_address = 'smtp.gmail.com'
smtp_port = 465
email_address = FOR
email_password = PASSWORD
email_receiver = TO

for i in range(len(precio1)):
    if (precio1[i] != precio2[i]):
        link = link1[i]
        rebaja = precio1[i]-precio2[i]
        precio = precio2[i]

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            # connect to mail
            server.login(email_address, email_password)
            # send mail
            msg='A product has been reduced in price, it has been reduced by a total of {0}$, it now costs {1}. \nLink: {2}'.format(rebaja, precio, link)
            server.sendmail(email_address, email_receiver, msg)
        sleep(0.1)
    else:
        sleep(0.1)

if os.path.exists('search.csv'):
    os.remove('search.csv')
