import argparse
import pathlib
import sys

from organizer.organizer import Organizer
# from organizer.DirectoryTree import DirectoryTree

from . import __version__


def main():
    args = parse_cli_args()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The mentioned directory doesn't exist.")
        sys.exit(1)

    file_organizer = Organizer(root_dir=root_dir)
    file_organizer.organize()
    # tree = DirectoryTree(root_dir=root_dir)
    # tree.generate()


def parse_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="organizer", description="a file organizer application to sort files based on media types")
    parser.version = __version__

    parser.add_argument("--version", "-v", action="version")

    parser.add_argument("--root-dir", "-d", metavar="ROOT_DIR",
                        default=".", help="Name of the directory whose files are to be sorted", nargs="?")

    return parser.parse_args()
