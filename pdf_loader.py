import requests
from pypdf import PdfReader
import io


def download_pdf(url: str) -> str:
response = requests.get(url)
response.raise_for_status()
return response.content


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
reader = PdfReader(io.BytesIO(pdf_bytes))
text = ""
for page in reader.pages:
text += page.extract_text() + "\n"
return text
