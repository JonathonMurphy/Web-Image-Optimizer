#!/usr/bin/env python3
import sys, os
from PIL import Image
from pathlib import Path

outputExtensions = ["jpg", "png", "jp2", "webp"]
filePath = Path(sys.argv[1])

def exportImages(file):
    img = Image.open(file)
    filename, extension = os.path.splitext(os.path.basename(file))
    fileExtensions = outputExtensions[:]
    fileExtensions.remove(extension[1:])
    for fileExtension in fileExtensions:
        if os.path.isdir(f"{filePath}/{fileExtension}"):
            img.save(f"{filePath}/{fileExtension}/{filename}.{fileExtension}")
        else:
            os.mkdir(f"{filePath}/{fileExtension}")
            img.save(f"{filePath}/{fileExtension}/{filename}.{fileExtension}")

for file in filePath.iterdir():
    exportImages(file)
