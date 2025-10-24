import argparse

import project.constants as C


def main() -> int:
    parser = argparse.ArgumentParser(prog="project", description="")

    # https://stackoverflow.com/a/8521644/812183
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {C.VERSION}",
    )
    args = parser.parse_args()
    print(args)

    return 1
