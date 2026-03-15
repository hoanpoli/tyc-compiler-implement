import pypdf
import sys

def extract_pdf(file_path):
    print(f"\n--- EXTRACTING {file_path} ---")
    try:
        reader = pypdf.PdfReader(file_path)
        text = ""
        for i, page in enumerate(reader.pages):
            text += f"Page {i+1}:\n" + page.extract_text() + "\n"
        print(text[:2000]) # View first 2000 chars to get an idea
        with open(file_path + ".txt", "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"Error: {e}")

extract_pdf("document/sliders/fp-python.pdf")
extract_pdf("document/sliders/oop-handout.pdf")
extract_pdf("document/sliders/oop-python.pdf")
