import time
import subprocess
from datetime import datetime
from config import *

print("Starting Linux Resource Monitor...")


def get_cpu_usage():
    output = subprocess.check_output("top -bn1 | grep 'Cpu(s)'", shell=True)
    usage = float(output.decode().split()[1])
    return usage

def get_memory_usage():
    output = subprocess.check_output("free | grep Mem", shell=True)
    parts = output.decode().split()
    used = float(parts[2])
    total = float(parts[1])
    return (used / total) * 100

def get_disk_usage():
    output = subprocess.check_output("df / | tail -1", shell=True)
    return float(output.decode().split()[4].replace('%',''))

def log_metrics(cpu, mem, disk):
    with open("logs/metrics.log", "a") as f:
        f.write(f"{datetime.now()} | CPU:{cpu:.2f}% MEM:{mem:.2f}% DISK:{disk:.2f}%\n")

def log_alert(message):
    with open("logs/alerts.log", "a") as f:
        f.write(f"ALERT | {datetime.now()} | {message}\n")

print(f"Monitoring started (interval={CHECK_INTERVAL}s)")
print("Press Ctrl+C to stop.")

try:
    while True:
        cpu = get_cpu_usage()
        mem = get_memory_usage()
        disk = get_disk_usage()

        log_metrics(cpu, mem, disk)

        print(
        f"[{datetime.now().strftime('%H:%M:%S')}] "
        f"CPU:{cpu:.1f}% MEM:{mem:.1f}% DISK:{disk:.1f}%"
        )


        if cpu > CPU_THRESHOLD:
            log_alert("CPU threshold exceeded")

        if mem > MEM_THRESHOLD:
            log_alert("Memory threshold exceeded")

        if disk > DISK_THRESHOLD:
            log_alert("Disk threshold exceeded")

        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("\nStopping Linux Resource Monitor...")
    log_alert("Monitor stopped by user (Ctrl+C)")
    print("Shutdown complete.")