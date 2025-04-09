import requests
import os

pdf_dir = input("Enter the directory path containing PDF files: ")

pdf_files = []
for file_name in os.listdir(pdf_dir):
    if file_name.endswith(".pdf"):
        pdf_files.append(('pdf_files', open(os.path.join(pdf_dir, file_name), 'rb')))

if not pdf_files:
    print("No PDF files found in the specified directory.")
else:
    url = "http://127.0.0.1:8000/books/add/"
    response = requests.post(url, files=pdf_files)

    if response.status_code == 201:
        print("Books added successfully!")
    else:
        print(f"Failed to add books: {response.text}")
