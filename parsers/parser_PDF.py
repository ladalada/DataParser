from tika import parser
import re


def pdf_parser(pdf_name):
    try:
        parsedPDF = parser.from_file(pdf_name)
    except FileNotFoundError:
        return 'no such file'
    
    current_pdf = parsedPDF["content"]
    filtered_pdf = re.sub(r'\\n', '', current_pdf)
    return filtered_pdf


