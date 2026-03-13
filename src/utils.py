#!/usr/bin/env python

import zipfile
from pathlib import Path


def create_zip_archive(files_dict, output_path):
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for arcname, filepath in files_dict.items():
            zipf.write(filepath, arcname=arcname)
