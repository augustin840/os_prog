import platform
import os
import time
from datetime import datetime
import psutil


def get_system_info():
    os_info = platform.uname()
    os_version = os_info.version
    computer_processor_info = os_info.machine, os_info.processor
    computer_name = os_info.node
    system_time = time.strftime("%H:%M:%S", time.gmtime())
    local_time = datetime.now().strftime("%H:%M:%S")

    print(f"OS: {os_info.system} {os_info.release}")
    print(f"OS version: {os_version}")
    print(f"Computer processor information: {computer_processor_info}")
    print(f"Computer Name: {computer_name}")
    print(f"System Time: {system_time}")
    print(f"Local Time: {local_time}")

    drives = [partition.device for partition in psutil.disk_partitions()]
    print("Available Drives: ", drives)

    for drive in drives:
        usage = psutil.disk_usage(drive)
        total = usage.total
        used = usage.used
        free = usage.free
        print(f"Drive {drive}: Total: {total} bytes, Used: {used} bytes, Free: {free} bytes")


def list_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                info = entry.stat()
                print(
                    f"{entry.name} - Size: {info.st_size} bytes, Created: {datetime.fromtimestamp(info.st_ctime)}, Modified: {datetime.fromtimestamp(info.st_mtime)}")
    except FileNotFoundError:
        print("The system cannot find the path specified.")


def main():
    get_system_info()
    path = input("Enter the drive or folder path to list contents: ")
    list_directory_contents(path)


if __name__ == "__main__":
    main()
