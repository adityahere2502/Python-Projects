import fitz  # PyMuPDF
from PIL import Image

def pdf_to_images(pdf_file, output_folder, image_format='png'):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        
        # Convert the PDF page to an image
        pix = page.get_pixmap()

        # Create a PIL image from the pixmap
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image to the output folder
        image.save(f"{output_folder}/page_{page_number + 1}.{image_format}")

    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    pdf_file = "example.pdf"  # Replace with the path to your PDF file
    output_folder = "output_images"  # Replace with the folder where you want to save the images
    image_format = "png"  # Change this to the desired image format (e.g., 'jpg', 'png', 'bmp', etc.)

    pdf_to_images(pdf_file, output_folder, image_format)
