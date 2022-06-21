'''
pip install watchdog
'''

import os,time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# 序号
i = 0

class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        filename = os.path.basename(event.src_path)
        extension = filename.split(".")[-1]  # file.jpg
        new_filename = "{:02d}_{}".format(i, filename)  # 00_file.jpg
        #new_filename = "{:02d}.{}".format(i, extension) # 00.jpg
        os.rename(filename, new_filename)
        print(f"created: {filename}")

    def on_deleted(self, event):
        print("deleted: " + event.src_path)

    def on_modified(self, event):
        print("modified: " + event.src_path)

    def on_moved(self, event):
        print("moved/renamed: " + event.src_path)


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
