import os
import random
import string
import requests

# Configuration
API_URL = 'http://localhost:8000/books/'  # Replace with your server's URL
PDF_FOLDER = '/home/rak/books/assambler'  # Folder containing the PDFs you want to send
NUM_BOOKS = 1000  # Number of books to send

# Function to generate a random string (optional, if you want to name the PDFs randomly)


# Function to send book PDF to the API
def send_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        files = {
            'pdf': (os.path.basename(pdf_path), pdf_file, 'application/pdf'),
        }

        response = requests.post(API_URL, files=files)
        if response.status_code == 201:
            print(f"Successfully uploaded: {pdf_path}")
        else:
            print(f"Failed to upload: {pdf_path} - {response.status_code}, {response.text}")

# Main function to send only PDFs from the folder
def main():
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]
    
    for i, pdf_file in enumerate(pdf_files[:NUM_BOOKS]):
        pdf_path = os.path.join(PDF_FOLDER, pdf_file)
        send_pdf(pdf_path)

if __name__ == '__main__':
    main()
