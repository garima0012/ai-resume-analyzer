"""
parser.py – Extract raw text from PDF and DOCX resume files.
"""
import io


def extract_text_from_pdf(file) -> str:
    """Extract text from an uploaded PDF file object."""
    try:
        import pdfplumber

        text_parts = []
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        return "\n".join(text_parts)
    except ImportError:
        # Fallback using PyPDF2
        try:
            import PyPDF2

            reader = PyPDF2.PdfReader(file)
            return "\n".join(
                page.extract_text() or "" for page in reader.pages
            )
        except Exception as e:
            return f"[Error reading PDF: {e}]"


def extract_text_from_docx(file) -> str:
    """Extract text from an uploaded DOCX file object."""
    try:
        import docx

        doc = docx.Document(io.BytesIO(file.read()))
        return "\n".join(para.text for para in doc.paragraphs if para.text.strip())
    except Exception as e:
        return f"[Error reading DOCX: {e}]"
