import PyPDF2

def split_pdf(input_pdf_path, output_dir):
    pdf = PyPDF2.PdfReader(input_pdf_path)

    for page_number in range(len(pdf.pages)):
        output_pdf = PyPDF2.PdfWriter()
        output_pdf.add_page(pdf.pages[page_number])

        output_pdf_path = f"{output_dir}/main_{page_number + 1}.pdf"
        with open(output_pdf_path, "wb") as output_file:
            output_pdf.write(output_file)
        print(f"Page {page_number + 1} saved to {output_pdf_path}")

if __name__ == "__main__":
    input_pdf_path = "main.pdf"  # Replace with your input PDF file path
    output_directory = "./"  # Replace with your desired output directory

    split_pdf(input_pdf_path, output_directory)
