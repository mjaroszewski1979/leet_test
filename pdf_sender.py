from datetime import datetime
from fpdf import FPDF



def get_pdf(company):
    today = datetime.now()
    new_pdf = FPDF()
    new_pdf.add_page()
    new_pdf.set_font('Helvetica', size = 12)
    new_pdf.set_margins(20.0, 20.0, 20.0)
    txt_1 = 'Maciej Jaroszewski' + '\r\n' + '511 826 318' + '\r\n' + 'mjaroszewski1979@gmail.com'
    txt_2 = today.strftime("%a,%d %b, %Y")
    txt_3 = company
    txt_4 = 'Dear Sirs,'
    txt_5 = 'This letter is to express my interest in the Software Developer position. I am excited about the opportunity to join your team and contribute my experiences to the company. In my previous roles, I learned how to handle multiple tasks efficiently, work well under pressure, and communicate effectively with both customers and colleagues. I also gained valuable problem-solving skills and the ability to learn new systems and technologies quickly. I have always been interested in computers and have taught myself the basics of programming. I am now eager to take my competence to the next level by learning from experienced professionals and working on real-world projects.'
    txt_6 = 'During my time as a Restaurant Manager i have acquired the ability to handle multiple tasks and prioritize work effectively. On many occasions it was necessary to deal with customer complaints and requests, which can be useful experience for working with clients in a software development role. My prime concern was ensuring that the restaurant ran smoothly and that all issues were addressed in a timely manner. Thanks to good organizational skills as well as a strong team work ethic, we were able to finish every project within the deadline.'
    txt_7 = 'In my current role I work in a group that is comprised of many different disciplines, therefore I need to be cognizant of their respective expertise and know when to yield to their discretion. We are using technical specifications on a daily basis which outlines the requirements and features that a product has to have in order to work as intended. Furthermore, my company rely on SAP as their core ERP platform, which has exposed me to new fields and strengthened my database management skills. As someone with assembly technical experience i have good understanding how different components fit together which can be valuable in working with complex systems.'
    txt_8 = "I would be grateful for the opportunity to discuss my qualifications further and learn more about the opportunities at {}. As a Software Developer, my goal is to continually increase my programming skills in order to present better solutions to my employers and their clients. I am particularly interested in working at {} because of your reputation for developing innovative products and technologies. I believe that my experience make me a strong fit for your team, and I am eager to be a part of your company's growth and success. Thank you for taking the time to review my cover letter and attached resume.".format(company, company)
    txt_9 = 'Kind Regards,'
    txt_10 = 'Maciej Jaroszewski'
    new_pdf.multi_cell(0, 5, txt_1)
    new_pdf.ln(5)
    new_pdf.multi_cell(0, 5, txt_2)
    new_pdf.ln(5)
    new_pdf.multi_cell(0, 5, txt_3)
    new_pdf.ln(10)
    new_pdf.multi_cell(0, 5, txt_4)
    new_pdf.ln(7)
    new_pdf.multi_cell(0, 5, txt_5)
    new_pdf.ln(5)
    new_pdf.multi_cell(0, 5, txt_6)
    new_pdf.ln(5)
    new_pdf.multi_cell(0, 5, txt_7)
    new_pdf.ln(5)
    new_pdf.multi_cell(0, 5, txt_8)
    new_pdf.ln(7)
    new_pdf.multi_cell(0, 5, txt_9)
    new_pdf.ln(10)
    new_pdf.multi_cell(0, 5, txt_10)
    new_pdf.output('Maciej_Jaroszewski_CL.pdf')


