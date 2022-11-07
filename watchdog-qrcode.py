'''
pip install watchdog
pip install qrcode qrtools Pillow pyzbar
pip install opencv-python
pip install opencv-contrib-python
'''

import os, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import qrcode
import cv2
from pyzbar.pyzbar import decode

file_path = ".\"

# 序号
i = 1

class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        global i

        # 重命名
        filename = os.path.basename(event.src_path)
        extension = filename.split(".")[-1]  # file.jpg
        new_filename = "{:02d}.{}".format(i, extension) # 00.jpg

        # 文件已存在
        while os.path.exists(os.path.join(file_path, new_filename)):
            i += 1
            new_filename = "{:02d}.{}".format(i, extension) # 00.jpg

        os.rename(filename, new_filename)
        print(f"created: {new_filename}")

        # 识别微信二维码
        try:
            data = cv2.wechat_qrcode_WeChatQRCode().detectAndDecode(cv2.imread(new_filename))[0][0]
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
    os.chdir(file_path)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
