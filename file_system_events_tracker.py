import sys
import os
import time
import random
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = “C:/Users/sparsh/Downloads”

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'hey,{event.src_path} has been created!')

    def on_deleted(self, event)
        print(f'hey,someone deleted {event.src_path}!')

    def on_modified(self, event):
        print(f'hey,{event.src_path} has been Modified!')

    def on_moved(self, event):
        print(f'hey,{event.src_path} has been moved!')

if __name__ == "__main__":
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=from_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(2)
            print('running...')
    except KeyboardInterrupt:
        print('stopped')
        observer.stop()