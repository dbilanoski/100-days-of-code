'''
PDFs and Spreadsheets Puzzle Exercise

Let's test your skills, the files needed for this puzzle exercise

You will need to work with two files for this exercise and solve the following tasks:

    Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).
    Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can't download from Google Drive) and find the phone number that is in the document. Note: There are different ways of formatting a phone number!

Task One: Grab the Google Drive Link from .csv File



Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.
'''
# Imports
import os, csv, PyPDF2, re
from urllib import request

# Download the challenge csv from the repo
f_path = os.getcwd()+"\\15_PDF_and_Spreadsheets\\"
request.urlretrieve("https://raw.githubusercontent.com/Pierian-Data/Complete-Python-3-Bootcamp/master/15-PDFs-and-Spreadsheets/Exercise_Files/find_the_link.csv",f_path+"challenge_find_the_link.csv")

# Get the csv data
f_csv = open(f_path+"challenge_find_the_link.csv",mode="r",encoding="utf-8")
csv_reader = csv.reader(f_csv)
csv_list = list(csv_reader)

# Since it's letter by letter diagonally from top left to bottom right, we'll iterate and extract
drive_link = []
for index,item in enumerate(csv_list):
  # In each list item we are taking the current index of the sub list item (diagonal)
  drive_link.append(item[index])

f_csv.close()

# Download from gdrive link
# request.urlretrieve("".join(drive_link),f_path+"challenge_pdf.pdf")

# Get the PDF data
f_pdf = open(f_path+"challenge_pdf.pdf",mode="rb")
pdf_reader = PyPDF2.PdfFileReader(f_pdf)

# We'll put pages to a list
pdf_pages = []

for page in range(pdf_reader.numPages):
  current_page = pdf_reader.getPage(page)
  pdf_pages.append(current_page.extractText())

f_pdf.close()

# Now we built phone regex pattern and check the pages content

phone_pattern = r"\d{3}.\d{3}.\d{4}"
result = re.search(phone_pattern,"".join(pdf_pages))

print(result.group())

## RESULT: 505 503 4455