#===============================================================================
#  Install
#===============================================================================
#  pip install qrtools
#  pip install qrcode
#  pip install pyzbar
#  pip install pillow
#===============================================================================

import os
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

file_path = "./"

for file in os.listdir(file_path):

    if os.path.splitext(file)[-1].lower() not in ['.jpg', '.jpeg', '.png']: 
        continue

    try:
        data = decode(Image.open(file))[0][0].decode("utf-8")
        qr = qrcode.QRCode(version=4, box_size=5, border=0, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        img.save("_" + file)
        # os.remove(file)
    except:
        continue
