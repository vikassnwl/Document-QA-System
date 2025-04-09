# RUN THIS FILE TO DOWNLOAD EMBEDDING MODEL AND LLM

import os
from helpers import download, unpack_archive



models = [{"file_url": "https://mega.nz/file/qvAwiITR#rrOODkLdSJzq739zVOK9Mhm23HfYeE5BljS6JbAJJQA",
                     "file_name": "Llama-3.2-1B-Instruct-Q4_0.gguf"},
                    {"file_url": "https://mega.nz/file/7ngiCKrK#RTQaTm2c2JxOPpatykXy-p7H7OnwxTFeo8mN6f6GQBQ",
                     "file_name": "universal-sentence-encoder_4.zip"}]


for model in models:
    file_url = model["file_url"]
    model_dir = "models"
    file_save_path = os.path.join(model_dir, model["file_name"])
    download(file_url, file_save_path, download_from="mega", force=False)
    archive_exts = [".tar", ".tar.gz", ".tgz", ".zip"]
    if any([file_save_path.endswith(ext) for ext in archive_exts]):
        target_dir = os.path.join(model_dir, os.path.splitext(model["file_name"])[0])
        unpack_archive(file_save_path, target_dir=target_dir, force=False)

