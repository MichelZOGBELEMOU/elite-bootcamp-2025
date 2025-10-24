"""Main module"""
import argparse as ap
import monitor as m
from error import custom_error

def main() -> None:
    """The program entry point"""
    cpu =m.CpuMonitor()
    memory = m.MemoryMonitor()
    disk = m.DiskMonitor()
    parser = ap.ArgumentParser(prog="sysinfo.py",
                               description="Print the system monitoring",
                               epilog="For more information visit www.michelz.com",
                               )
    parser.error = lambda message: custom_error(parser)
    parser.add_argument('--cpu',help="Print the cpu usage in percentage", action="store_true")
    parser.add_argument('--mem', help="Print the memory usage in percentage", action="store_true")
    parser.add_argument('--disk', help="Print the disk usage in percentage", action="store_true")
    parser.add_argument("--all", help="Print all the monitoring of the system", action="store_true")
    parser.add_argument("-v", "--verbose", action='version', version='Sysinfo v1')

    args = parser.parse_args()
    if args.all or args.cpu:
        print(cpu.status())
    if args.all or args.mem:
        print(memory.status())
    if args.all or args.disk:
        print(disk.status())
    if args.verbose:
        print("version: v1.0.0")


if __name__ == "__main__":
    main()
