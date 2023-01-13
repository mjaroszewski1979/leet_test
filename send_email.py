import smtplib
import ssl
from email.message import EmailMessage
from pdf_sender import get_pdf
from email_content import get_content

import time

def send_email(company_name, company_email):
    get_pdf(company=company_name)
    time.sleep(5)
    content = get_content(company_name)


    smtp_port = 587
    smtp_server = 'smtp.gmail.com'
    email_from = 'mjaroszewski1979@gmail.com'
    email_to = company_email
    pswd = 'pass'
    simple_email_context = ssl.create_default_context()

    msg = EmailMessage()

    msg['Subject'] = 'Software Developer'
    msg['From'] = email_from
    msg['To'] = email_to
    msg.set_content(content, subtype='html')

    pdf_files = ['Maciej_Jaroszewski_CL.pdf', 'Maciej_Jaroszewski_CV.pdf']

    for pdf_file in pdf_files:


        with open(pdf_file, 'rb') as pdf:
            msg.add_attachment(pdf.read(), maintype='application', subtype='octet-stream', filename=pdf.name)

    try:
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from, pswd)
        TIE_server.send_message(msg)

    except Exception as e:
        print(e)

    finally:
        TIE_server.quit()
