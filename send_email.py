import smtplib
import ssl
from email.message import EmailMessage
from pdf_sender import get_pdf
import time

def send_email(company_name, company_email):
    get_pdf(company=company_name)
    time.sleep(5)

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
    msg.set_content('''
    <!DOCTYPE html>
    <html>
        <body>
            <div style="padding:10px 20px;text-align:justify;font-family:Georgia, 'Times New Roman', Times, serif;">
                <p>Dear Sirs,</p>
                <br>
                <br>
                <p>I am writing to express my interest in the software development opportunities at {}. I recently came across your company and was impressed by the innovative products and technologies you are working on.
                    Although I do not have a computer science degree, I have always been interested in technology and have spent the past few years teaching myself how to code in multiple programming languages, including AFL, MQL4 and Python.</p>
                <br>
                <p>I have completed a number of online courses and projects, including building a web application and developing algorithmic trading strategies. I am eager to start my career in software development and believe that {} would be a great place for me to grow and learn. I am confident that my enthusiasm for technology and strong work ethic make me a valuable asset to your team.
                    I am attaching my resume for your review. I would be grateful for the opportunity to discuss my qualifications further and learn more about the opportunities at {}. Thank you for considering my application.</p>
                <br>
                <p>Sincerely,</p>
                <br>
                <br>
                <h5>Maciej Jaroszewski</h5>
                <p><span style="font-size:smaller;color:grey;">mjaroszewski.website</span><p/>
                <p><span style="font-size:smaller;color:grey;">github.com/mjaroszewski1979</span><p/>
            </div>
        </body>
    </html>
    '''.format(company_name, company_name, company_name), subtype='html')

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
