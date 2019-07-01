#!/usr/bin/env python3
from PIL import Image
import glob, os, sys

fileTypes = (".jpg", ".png", ".jp2", ",webp")
# Mutate the tuple depending on the file type of the selected file

def exportImages(file):
    Image.open(file).save(file + fileTypes[1], )
    Image.open(file).save(file + fileTypes[2])
    Image.open(file).save(file + fileTypes[3])


for infile in glob.glob(sys.argv[1]):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.save(file + ".thumbnail" + ".jpg", "JPEG")
    im.save(file + '.webp')
    im.save(file + ".jp2")
    im.save(file + ".png")
