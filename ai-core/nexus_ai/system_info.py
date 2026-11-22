
import os
import platform
import shutil
from pathlib import Path


def get_os_info():
    """Return operating system information."""
    info = {
        "system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "hostname": platform.node(),
    }

    os_release = Path("/etc/os-release")
    if os_release.exists():
        for line in os_release.read_text().splitlines():
            if line.startswith("PRETTY_NAME="):
                info["distribution"] = line.split("=", 1)[1].strip('"')
                break

    return info


def get_cpu_info():
    """Return basic CPU information."""
    cpu_name = platform.processor()

    if not cpu_name:
        cpu_file = Path("/proc/cpuinfo")

        if cpu_file.exists():
            for line in cpu_file.read_text().splitlines():
                if line.startswith("model name"):
                    cpu_name = line.split(":", 1)[1].strip()
                    break

    return {
        "processor": cpu_name or "Unknown",
        "logical_cores": os.cpu_count() or 1,
    }

def get_memory_info():
    """Return memory information in MB."""
    memory_file = Path("/proc/meminfo")

    if not memory_file.exists():
        return {"available": False}

    memory = {}

    for line in memory_file.read_text().splitlines():
        if line.startswith(("MemTotal:", "MemAvailable:")):
            key, value = line.split(":", 1)
            memory[key] = int(value.strip().split()[0]) // 1024

    return {
        "total_mb": memory.get("MemTotal"),
        "available_mb": memory.get("MemAvailable"),
    }


def get_disk_info():
    """Return disk capacity information in GB."""
    disk = shutil.disk_usage("/")

    return {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
    }


def get_system_report():
    """Collect all available system information."""
    return {
        "operating_system": get_os_info(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
    }
