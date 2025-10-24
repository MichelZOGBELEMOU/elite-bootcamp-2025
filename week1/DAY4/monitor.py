"""A module that describe a basic system monitor hierarchy"""
import os
import psutil as ps
from psutil._common import bytes2human

class SystemMonitor():
    """Represente a base system monitoring"""
    def __init__(self) -> None:
        """Initialize a system monitoring by giving setting 
        a hostname and the operating system and version"""
        # Manage only linux systems
        if hasattr(os, "uname"):
            self.hostname = os.uname().nodename
        else:
            self.hostname = "Other"
    def status(self) -> str:
        """methods to compute the status 
        Returns:
            the status: str
        """
        return "Base Monitor"


class CpuMonitor(SystemMonitor):
    """Represente a cpu monitoring"""
    def __init__(self) -> None:
        super().__init__()
        self.cpu_max_freq = ps.cpu_freq().max
        self.number_of_cpu = ps.cpu_count()
    def status(self) -> str:
        """Method to compute and return usage of the cpu
        in percentage.
        Return:
            formated string  for the cpu usage in percentage"""
        return f"CPU USAGE: {ps.cpu_percent(interval=1)} %"

class MemoryMonitor(SystemMonitor):
    """Represent the memory monitoring"""
    def __init__(self) -> None:
        """Initialize a memory Monitoring"""
        super().__init__()
        self.mem_giga = bytes2human(ps.virtual_memory().total)

    def status(self) -> str:
        """Method to compute and return usage of the memory in percentage
        Returns:
            A formated string for the memory usage"""
        return f"Memory Usage: {ps.virtual_memory().percent}%"

class DiskMonitor(SystemMonitor):
    """Represent the Disk monitoring"""
    def __init__(self) -> None:
        """Initialize a Disk Monitoring"""
        super().__init__()
        self.disk_total = ps.disk_usage('/').total

    def status(self) -> str:
        """Method to compute and return usage of disk in percentage
        Returns:
                A formated string for the disk usage"""
        return f"Disk Usage: {ps.disk_usage('/').percent}%"
    