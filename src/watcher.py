import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

WATCH_DIR = r"C:\temp\watch_folder"
LOG_FILE = r"C:\temp\file_watcher.log"
EXEC_SCRIPT = r"src\executor.bat"

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(f"Yeni dosya algılandı: {event.src_path}\n")

            # Windows için BAT çalıştırma
            subprocess.run(
                [EXEC_SCRIPT, event.src_path],
                shell=True
            )

if __name__ == "__main__":
    os.makedirs(WATCH_DIR, exist_ok=True)

    observer = Observer()
    observer.schedule(WatcherHandler(), WATCH_DIR, recursive=False)
    observer.start()

    print("📂 Klasör izleniyor:", WATCH_DIR)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
