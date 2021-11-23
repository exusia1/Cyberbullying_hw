import os.path
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)

    def on_deleted(self, event):
        print(event)

    def on_moved(self, event):
        print(event)


def list_drives():
    disk_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ['%s:' % d for d in disk_names if os.path.exists('%s:' % d)]


def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference


def supervise(path):
    print('Press Ctrl+C to return to USB supervision')
    observer = Observer()
    observer.schedule(Handler(), path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


old_drives = list_drives()
print(f'Initial drives {old_drives}')

while True:
    time.sleep(10)
    drives_now = list_drives()
    new_drives = diff(drives_now, old_drives)
    if new_drives:
        print(f'New drive: {str(new_drives[0])}, initializing file watcher')
        supervise(new_drives[0])
    else:
        print('no new drives')

    old_drives = drives_now
