import sys,re,os
from qrtools import *
from qrcode import *
from pyzbar.pyzbar import decode
from PIL import Image

file_path = "./"

for each_image in os.listdir(file_path):

    image_type = os.path.splitext(each_image)[-1].lower()
    
    if image_type not in ['.jpg', '.jpeg', '.png']: 
        continue

    try:
        data = decode(Image.open(each_image))[0][0].decode("utf-8")
    except:
        continue
    
    qr = QRCode(version=4, box_size=5, border=0, error_correction=ERROR_CORRECT_L)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.resize((128, 128), Image.ANTIALIAS)
    img.save(each_image.split("_")[0] +".png")

    os.remove(each_image)
