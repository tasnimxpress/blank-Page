from PyPDF2 import PdfMerger
import os

def merge_pdfs_with_blank(input_folder, output_folder):
    # Create the output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each folder in the input folder
    for folder in os.listdir(input_folder):
        folder_path = os.path.join(input_folder, folder)

        # Check if the item in the folder is a directory
        if os.path.isdir(folder_path):
            pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
            pdf_files.sort()

            # Get the name of the PDF file
            if pdf_files:
                pdf_name = os.path.splitext(pdf_files[0])[0]
            else:
                continue

            output_file = os.path.join(output_folder, f"{pdf_name}_merged.pdf")

            merger = PdfMerger()

            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)

                merger.append(pdf_path)

            # Save merged PDF to the output folder
            merger.write(output_file)
            merger.close()

# if __name__ == "__main__":
#     input_folder = "Input Folder"
#     output_folder = "Merged_folder"
#
#     merge_pdfs_with_blank(input_folder, output_folder)
