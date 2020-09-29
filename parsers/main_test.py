from parser_DOCX import document_parser
from parser_HTML import html_text, html_links
from parser_PDF import pdf_parser

#test right answer if document is absent
def test_document_absent():
    document_name = 'fail.docx'
    real_answer = "There is no data..."
    assert document_parser(document_name) == real_answer

#test right answer if link is absent
def test_empty_html_link():
    test_link = ''
    real_answer = 'no such site'
    assert html_text(test_link) == real_answer
    assert html_links(test_link) == real_answer

#test right answer if link is not valid
def test_no_valid_html_link():
    test_link = 'my.html'
    real_answer = 'no such site'
    assert html_text(test_link) == real_answer
    assert html_links(test_link) == real_answer

#test right answer if link is right
def test_valid_html_link():
    test_link = 'https://stackoverflow.com/questions/34363388/pytest-no-tests-ran'
    assert html_text(test_link) != 'no such site'
    assert html_links(test_link) != 'no such site'

#test right answer if pdf file is absent
def test_not_valid_pdf():
    document_name = 'my_file.pdf'
    result = 'no such file'
    assert pdf_parser(document_name) == result

