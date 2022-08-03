'''
pip install watchdog
pip install qrcode qrtools Pillow pyzbar
'''

import os, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# 序号
i = 1

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        global i
        filename = os.path.basename(event.src_path)
        ext = os.path.splitext(filename)[-1]
        newname = f"{i}{ext}"

        try:
            data = decode(Image.open(filename))[0][0].decode("utf-8")
            qr = qrcode.QRCode(version=4, box_size=5, border=0, error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image()
            img.save("_" + filename)
            os.remove(filename)
            
            os.rename("_" + filename, newname)
            print(f"{newname}")
            i += 1
        except:
            pass

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(event_handler=MyHandler(), path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
