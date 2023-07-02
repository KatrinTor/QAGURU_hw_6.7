import os
from conftest import RES_DIR
from pypdf import PdfReader

def test_read_pdf():
    pdf_file = os.path.join(RES_DIR, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_file)

    assert len(reader.pages) == 412
    assert 'pytest Documentation' in reader.pages[0].extract_text()
