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


file_path = ".\"

# 序号
i = 1

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        global i

        print(event.src_path)
        os.chdir(file_path)
        filename = os.path.basename(event.src_path)
        extension = filename.split(".")[-1]  # file.jpg
        new_filename = "{:02d}.{}".format(i, extension) # 00.jpg
        os.rename(filename, new_filename)
        print(f"created: {new_filename}")        

        try:
            data = decode(Image.open(new_filename))[0][0].decode("utf-8")
            qr = qrcode.QRCode(version=4, box_size=5, border=0, error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(new_filename)
        except:
            pass

        i += 1

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(event_handler=MyHandler(), path=file_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
