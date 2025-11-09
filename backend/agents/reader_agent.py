from PyPDF2 import PdfReader
from docx import Document

class ReaderAgent:
    def extract_text(self, content: bytes, filename: str) -> str:
        ext = filename.split(".")[-1].lower()

        try:
            if ext == "pdf":
                from io import BytesIO
                reader = PdfReader(BytesIO(content))
                text = "\n".join([p.extract_text() or "" for p in reader.pages])
                return text.strip() or "No readable text found in this PDF file."

            elif ext == "docx":
                from io import BytesIO
                doc = Document(BytesIO(content))
                text = "\n".join([p.text for p in doc.paragraphs])
                return text.strip() or "No readable text found in this DOCX file."

            elif ext == "txt":
                return content.decode("utf-8", errors="ignore").strip() or "No readable text found."

            else:
                return "Unsupported file format."

        except Exception as e:
            print(f"[ReaderAgent] Error: {e}")
            return "Error extracting text."
