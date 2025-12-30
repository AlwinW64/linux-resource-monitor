import subprocess
import time
from datetime import datetime
from config import *

#CPU Usage

def get_cpu_usage():
    output = subprocess.check_output(
        "top -bn1 | grep 'Cpu(s)'",
        shell=True
    ).decode()

    # Example line:
    # Cpu(s):  7.3 us,  1.2 sy,  0.0 ni, 91.0 id, ...
    idle = float(output.split("id")[0].split()[-1])
    return 100 - idle

#Memory Usage

def get_memory_usage():
    output = subprocess.check_output(
        "free | grep Mem",
        shell=True
    ).decode().split()

    total = float(output[1])
    used = float(output[2])
    return (used / total) * 100

#Disk Usage

def get_disk_usage():
    output = subprocess.check_output(
        "df / | tail -1",
        shell=True
    ).decode().split()

    return float(output[4].replace('%', ''))


if __name__ == "__main__":
    print(f"CPU: {get_cpu_usage():.2f}%")
    print(f"MEM: {get_memory_usage():.2f}%")
    print(f"DISK: {get_disk_usage():.2f}%")

