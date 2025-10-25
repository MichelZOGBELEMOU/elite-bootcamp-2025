"""Module defining the custom error function"""
import argparse
import sys
def custom_error(parser: argparse.ArgumentParser) -> None:
    """Custom error handler that prints help message and exit"""
    parser.print_help()
    sys.exit(2)
