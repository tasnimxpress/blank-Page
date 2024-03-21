import os
import PyPDF2

def add_blank_page_to_pdfs_in_subfolders(input_folder, output_folder):
    # Loop through each subfolder in the input folder
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                output_file = os.path.join(output_folder, f"Amended_{file}")

                with open(pdf_path, 'rb') as pdf_file:
                    # Read the input PDF
                    pdf_reader = PyPDF2.PdfReader(pdf_file)

                    # Create a PdfWriter object to append pages
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.append_pages_from_reader(pdf_reader)

                    # Add a blank page at the end of the PDF
                    pdf_writer.add_blank_page()

                    # Write the modified PDF to the output file in the output folder
                    with open(output_file, 'wb') as out_stream:
                        pdf_writer.write(out_stream)

                print(f"Amended file saved: {output_file}")

# if __name__ == "__main__":
#     input_folder = "Merged_folder"
#     output_folder = "Output folder"
#     add_blank_page_to_pdfs_in_subfolders(input_folder, output_folder)
