import os
import zipfile
import tarfile
from tqdm import tqdm

def unpack_archive(file_path, target_dir=None, force=False):
    target_dir = target_dir or (os.path.dirname(file_path) if os.path.dirname(file_path) else ".")
    
    # Determine archive type and get root dir
    if file_path.endswith(".zip"):
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            members = zip_ref.namelist()
            root_dir = members[0].split("/")[0]
    elif file_path.endswith((".tar", ".tar.gz", ".tgz")):
        with tarfile.open(file_path, "r") as tar_ref:
            members = tar_ref.getnames()
            root_dir = members[0].split("/")[0]
    else:
        print("Unsupported file type")
        return

    # unpacked_dir = os.path.join(target_dir, root_dir)
    unpacked_dir = target_dir
    print(f"Unpacking {file_path} to {target_dir}...")
    if os.path.exists(unpacked_dir) and not force:
        print(f"{unpacked_dir} already exists. Skipping unpacking.\n")
        return

    # Unpack with progress bar
    if file_path.endswith(".zip"):
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            for member in tqdm(members, desc="Extracting", unit="file"):
                zip_ref.extract(member, target_dir)
    elif file_path.endswith((".tar", ".tar.gz", ".tgz")):
        with tarfile.open(file_path, "r") as tar_ref:
            for member in tqdm(members, desc="Extracting", unit="file"):
                tar_ref.extract(member, target_dir)

    print(f"Archive unpacked to {unpacked_dir}\n")
    return unpacked_dir
