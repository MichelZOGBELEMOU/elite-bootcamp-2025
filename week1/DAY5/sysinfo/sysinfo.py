"""Main module"""
import argparse as ap
from datetime import datetime
import logging
import logging.handlers
import utils.errors as ce
import utils.monitor as m

def main() -> None:
    """The program entry point"""
    # Configuration
    LOG_FILE = "logs/sysinfo.log"
    MAX_FILE_SIZE_BYTES = 100 * 1024 # 100KB
    BACKUP_FILE_COUNT = 3

    # Create the instances of Monitor
    cpu =m.CpuMonitor()
    memory = m.MemoryMonitor()
    disk = m.DiskMonitor()

    # Create an argument parser object
    parser = ap.ArgumentParser(prog="sysinfo.py",
                               description="Print the system monitoring",
                               epilog="For more information visit www.michelz.com",
                               )
    # Affect the output of the custom error to the parser error
    # So that the help menu is display every time there is an error
    parser.error = lambda message: ce.custom_error(parser)

    # Add arguments to the parser
    parser.add_argument('--cpu',help="Print the cpu usage in percentage", action="store_true")
    parser.add_argument('--mem', help="Print the memory usage in percentage", action="store_true")
    parser.add_argument('--disk', help="Print the disk usage in percentage", action="store_true")
    parser.add_argument("--all", help="Print all the monitoring of the system", action="store_true")
    parser.add_argument("-v", "--verbose", action='version', version='Sysinfo v1')
    

    # Parse the arguments
    args = parser.parse_args()

    # Create the logger object
    logger = logging.getLogger("SYSINFO LOG FILE")
    logger.setLevel(logging.INFO)

    # Create the handler and format the log

    handler = logging.handlers.RotatingFileHandler(filename=LOG_FILE, maxBytes=MAX_FILE_SIZE_BYTES, backupCount=BACKUP_FILE_COUNT)
    formater = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formater)

    #add handler to the logger
    logger.addHandler(handler)
    logger.info(f"======Sysinfo execution started======")
    logger.info(f"Timestamp: {datetime.now():%Y-%m-%d %H:%M:%S}")
    logger.info(f"Command executed: {vars(args)}")
    try:
        result =[]
        if args.all or args.cpu:
            result.append(cpu.status())
        if args.all or args.mem:
            result.append(memory.status())
        if args.all or args.disk:
            result.append(disk.status())
        if args.all or args.verbose:
            result.append("Version v1")
            
        
        
        output = " | ".join(result)
        logger.info(f"System info: {output}")
        logger.info(f"Sysinfo executed successfully.\n")
    except Exception as e:
        logger.error(f"Error during execution: {e}", exc_info=True)
        print(f"Error {e}")


if __name__ == "__main__":
    main()
