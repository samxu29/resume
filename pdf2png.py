# pip3 install PyMuPDF Pillow

import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_to_png(pdf_path, output_folder):
    # Open the PDF file using PyMuPDF
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page in the PDF
    for page_number in range(len(pdf_document)):
        # Get a specific page
        page = pdf_document.load_page(page_number)
        
        # Convert the page to an image
        image = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        
        # Create a Pillow image from the raw image data
        pillow_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        
        # Save the image as a PNG file
        image_filename = f"{output_folder}/page_{page_number + 1}.png"
        pillow_image.save(image_filename, "PNG")

    # Close the PDF file
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = "shengkaixu_2023resume.pdf"  # Replace with the path to your PDF file
    output_folder = "pdf2png"  # Output folder where PNG images will be saved

    convert_pdf_to_png(input_pdf_path, output_folder)
