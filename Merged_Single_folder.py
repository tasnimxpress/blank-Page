import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_folder):
    # dictionary to store PDF
    pdf_dict = {}

    # Iterate all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(input_folder, filename)

            try:
                # open the PDF file
                with open(file_path, 'rb') as pdf_file:
                    # prefix before the underscore
                    prefix = filename.split('_')[0]

                    # If prefix is not in the dictionary, create a list
                    if prefix not in pdf_dict:
                        pdf_dict[prefix] = []

                    # Add file path to the prefix in the dictionary
                    pdf_dict[prefix].append(file_path)

            except Exception as e:
                print(f"Error processing file '{file_path}': {str(e)}")
                continue

    # Iterate the dictionary and merge
    for prefix, pdf_list in pdf_dict.items():
        merger = PdfMerger()

        # Sort and merge in order
        pdf_list.sort()

        for pdf_file in pdf_list:
            try:
                merger.append(pdf_file)
            except Exception as e:
                print(f"Error appending file '{pdf_file}' to the merger: {str(e)}")
                continue

        # output file path
        output_filename = os.path.join(output_folder, f"{prefix}_merged.pdf")

        # merged PDF to the output file
        with open(output_filename, "wb") as output_file:
            merger.write(output_file)

        merger.close()

# if __name__ == "__main__":
#     input_folder = "copy_consituency_138_to_162"
#     output_folder = "NewMergedFiles"
#
#     merge_pdfs(input_folder, output_folder)
