import pyttsx3
import PyPDF2
import pdfplumber

# path of the pdf file to read
file = "C:/Users/PC 01/Desktop/Portfolio/AutomationPythonScripts/ConvertPdfToAudio/sample.pdf"
f = open(file, "rb")
pdfR = PyPDF2.PdfReader(f)
pages = len(pdfR.pages) # Get the number of pages

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        
        s = pyttsx3.init()
        s.save_to_file(text, "C:/Users/PC 01/Desktop/Portfolio/AutomationPythonScripts/ConvertPdfToAudio/audio.mp3")
        s.runAndWait()
f.close()