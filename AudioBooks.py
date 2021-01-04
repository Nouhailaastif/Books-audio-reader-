# Import the packages needed
import pyttsx3
import PyPDF2

# After loading the file in the directory
# we're going to read the pdf
speaker = pyttsx3.init()
book = open('YOUR BOOK.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(book)
# store the pages of the book

pages = pdf.numPages

# a loop to extract the text and read it

for num in range(7, pages):

    page = pdf.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
