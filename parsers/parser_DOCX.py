from docx import Document


def document_parser(document_name):
    result = ''
    try:
        docx = Document(document_name)
        for para in docx.paragraphs:
            result += para.text
            result += '\n'
    except Exception:
        result = "There is no data..."
    return result