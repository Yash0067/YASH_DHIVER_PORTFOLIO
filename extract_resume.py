import PyPDF2

pdf_path = r"c:\Users\yash\Downloads\Yash_Dhiver_FullStack_Developer_Resume..pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
print(text)
