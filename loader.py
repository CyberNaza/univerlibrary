import requests
import os
import json

# Ask the user for the directory containing the PDF files
pdf_dir = input("Enter the directory path containing PDF files: ")

# List all PDF files in the directory
pdf_files = []
for file_name in os.listdir(pdf_dir):
    if file_name.endswith(".pdf"):
        pdf_files.append({"pdf": file_name})

# Check if there are any PDF files found
if not pdf_files:
    print("No PDF files found in the specified directory.")
else:
    # Send the JSON data to the API
    url = "http://127.0.0.1:8000/books/add/"
    response = requests.post(url, json=pdf_files)

    if response.status_code == 201:
        print("Books added successfully!")
    else:
        print(f"Failed to add books: {response.text}")
