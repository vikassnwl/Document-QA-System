import requests
import os
from mega import Mega
from tqdm import tqdm
import gdown



def download(file_url, file_save_path, download_from="drive", force=False):
    dest_path = os.path.dirname(file_save_path)
    dest_filename = os.path.basename(file_save_path)
    print(f"Downloading {dest_filename} to {dest_path}/...")
    if os.path.exists(file_save_path) and not force:
        # print("File already exists!\n")
        print(f"{file_save_path} already exists. Skipping download.\n")
        return
    
    if dest_path:
        os.makedirs(dest_path, exist_ok=True)

    if download_from == "web":
        response = requests.get(file_url, stream=True)
        total_size = int(response.headers.get("content-length", 0))

        with open(file_save_path, "wb") as file:
            with tqdm(total=total_size, unit="B", unit_scale=True) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
                    bar.update(len(chunk))
    elif download_from == "mega":
        # Initialize Mega object
        mega = Mega()
        # Download the file
        file = mega.download_url(file_url, dest_path=(dest_path or "."), 
                        dest_filename=dest_filename)
        print(f"File downloaded at {file}\n")
    else:
        FILE_ID = file_url.split("/")[-2]
        download_url = f"https://drive.google.com/uc?id={FILE_ID}&export=download"
        gdown.download(download_url, file_save_path)