import os

def has_subfolders(folder):
    """
    Check if a folder contains subfolders.
    """
    for _, dirs, _ in os.walk(folder):
        if dirs:
            return True
    return False

if __name__ == "__main__":
    input_folder = "Input Folder"
    output_folder_merge = "Merged_folder"
    output_folder_add_blank = "Output folder"

    if has_subfolders(input_folder):
        #for subfolders
        from Add_blank_page_for_subfolder import add_blank_page_to_pdfs_in_subfolders
        from merge_file_for_subfolder import merge_pdfs_with_blank

        # Merge the PDF files
        merge_pdfs_with_blank(input_folder, output_folder_merge)

        # Add blank page to the merged PDFs
        add_blank_page_to_pdfs_in_subfolders(output_folder_merge, output_folder_add_blank)
    else:
        #for single folder
        from Add_blank_page_single_folder import add_blank_page_to_pdfs_in_subfolders
        from Merged_Single_folder import merge_pdfs

        # Merge the PDF files
        merge_pdfs(input_folder, output_folder_merge)

        # Add blank page to the merged PDFs
        add_blank_page_to_pdfs_in_subfolders(output_folder_merge, output_folder_add_blank)
