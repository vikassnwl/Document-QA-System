# RUN THIS FILE TO DOWNLOAD SAMPLE DOCUMETNS FOR UPLOAD

import os
from helpers.download import download


sample_documents = [{"file_url": "https://mega.nz/file/K7AymIaR#vXYtKpypawhNcVmN-Hipu0_e79norvr1Ci7TMfazwVk",
                     "file_name": "Kidney-Stones-Patient-Guide.pdf"},
                    {"file_url": "https://mega.nz/file/miIlyIzZ#uvz43M86lvAhdPE6QBW-ZZS_CKD24c4nIj1_yrVj3hY",
                     "file_name": "budget_speech.pdf"}]


for sample_document in sample_documents:
    file_url = sample_document["file_url"]
    file_save_path = os.path.join("sample_documents", sample_document["file_name"])
    download(file_url, file_save_path, download_from="mega", force=False)
