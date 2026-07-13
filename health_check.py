#!/home/tidia/projets/interact-with-os/.venv/bin/python

import psutil
import shutil

def check_disk_usage(disk, min_free_percent=25):
    """Returns True if the disk usage is lower than the specified percentage."""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > min_free_percent

def check_cpu_usage(max_cpu_percent=75,interval_input=1,percpu_input=False):
    """Returns True if the CPU usage is lower than the specified percentage."""
    cpu_percent = psutil.cpu_percent(interval=interval_input, percpu=percpu_input)
    return cpu_percent < max_cpu_percent


if __name__ == "__main__":
    if not check_disk_usage("/", 25):
        print("ERROR: Not enough disk space")
    elif not check_cpu_usage(75,1):
        print("ERROR: CPU usage is over 75%")
    else:
        print("Everything is OK")


