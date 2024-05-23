import os
import shutil
from PIL import Image

def get_total_pages(tiff_file):
    """
    English:
    This function opens a TIFF file and counts the total number of pages.
    
    日本語:
    この関数は、TIFFファイルを開き、総ページ数をカウントします。
    """
    try:
        image = Image.open(tiff_file)
        total_pages = 0
        while True:
            try:
                image.seek(total_pages)
                total_pages += 1
            except EOFError:
                break
        return total_pages
    except Exception as e:
        print(f"Error processing file {tiff_file}: {e}")
        return 0

def extract_single_page_tiffs(source_folder, destination_folder):
    """
    English:
    This function recursively traverses the source folder, checking each TIFF file's page count and copying single-page TIFF files to the destination folder.
    
    日本語:
    この関数はソースフォルダーを再帰的にトラバースし、各TIFFファイルのページ数をチェックし、1ページのTIFFファイルを宛先フォルダーにコピーします。
    """
    print(f"Source folder: {source_folder}")
    print(f"Destination folder: {destination_folder}")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    single_page_files = []

    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return
    
    for root, dirs, files in os.walk(source_folder):
        print(f"Checking directory: {root}")
        for filename in files:
            file_path = os.path.join(root, filename)
            print(f"Found file: {file_path}")
            if filename.lower().endswith('.tif') or filename.lower().endswith('.tiff'):
                total_pages = get_total_pages(file_path)
                print(f"File: {filename}, Total Pages: {total_pages}")
                if total_pages == 1:
                    single_page_files.append(file_path)
                    destination_path = os.path.join(destination_folder, os.path.relpath(file_path, source_folder))
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    shutil.copy(file_path, destination_path)
                    print(f"Copied: {file_path} to {destination_path}")

    print(f"Total single-page TIFF files: {len(single_page_files)}")

def main():
    """
    English:
    Main function to define source and destination folders and initiate the extraction process.
    
    日本語:
    ソースフォルダーと宛先フォルダーを定義し、抽出プロセスを開始するメイン関数。
    """
    source_folder = r"xxxxx"
    destination_folder = r"xxxx"

    # Ensure paths are absolute paths
    source_folder = os.path.abspath(source_folder)
    destination_folder = os.path.abspath(destination_folder)

    print(f"Resolved source folder: {source_folder}")
    print(f"Resolved destination folder: {destination_folder}")

    extract_single_page_tiffs(source_folder, destination_folder)

if __name__ == "__main__":
    main()
