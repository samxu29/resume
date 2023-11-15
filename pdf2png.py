import fitz 
from PIL import Image
import argparse

def convert_pdf_to_png(pdf_path, output_folder):
    
    pdf_document = fitz.open(pdf_path)
    
    for page_number in range(len(pdf_document)):
        
        page = pdf_document.load_page(page_number)
        
        image = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        
        pillow_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        
        image_filename = f"{output_folder}/{pdf_path}_{page_number + 1}.png"
        pillow_image.save(image_filename, "PNG")

    pdf_document.close()

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to PNG")
    parser.add_argument("pdf_path", help="Path to the input PDF file")
    parser.add_argument("output_folder", help="Path to the output folder where PNGs will be saved")

    args = parser.parse_args()

    convert_pdf_to_png(args.pdf_path, args.output_folder)

if __name__ == "__main__":
    main()
