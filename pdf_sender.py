from datetime import datetime
from fpdf import FPDF
from pdf_text import get_content, spaces


'''
This function is responsible for creating pdf file from seperate utility unit - pdf_text.
It has hard coded settings like font family and size as well as margins parameters.
It takes one argument - company name which is dynamically injected into pdf file.
For displaying current date this function uses datetime module combined with string formatting.
Finally it saves created pdf to output file located in working directory.

'''
def get_pdf(company):
    today = datetime.now()
    new_pdf = FPDF()
    new_pdf.add_page()
    new_pdf.set_font('Helvetica', size = 12)
    new_pdf.set_margins(20.0, 20.0, 20.0)

    pdf_content = get_content(company)
    for idx, el in enumerate(pdf_content):
        if el == 'tdy':
            new_pdf.multi_cell(0, 5, today.strftime("%a,%d %b, %Y"))
            new_pdf.ln(spaces[idx])
        elif el == 'cmp':
            new_pdf.multi_cell(0, 5, company )
            new_pdf.ln(spaces[idx])
        else:
            new_pdf.multi_cell(0, 5, el )
            new_pdf.ln(spaces[idx])

    new_pdf.output('Maciej_Jaroszewski_CL.pdf')


