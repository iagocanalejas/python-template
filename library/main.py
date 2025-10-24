import argparse

import library.constants as C


def main() -> int:
    parser = argparse.ArgumentParser(prog="library", description="")

    # https://stackoverflow.com/a/8521644/812183
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {C.VERSION}",
    )

    subparsers = parser.add_subparsers(dest="command")

    def _add_cmd(name: str, *, help: str) -> argparse.ArgumentParser:
        parser = subparsers.add_parser(name, help=help)
        return parser

    args = parser.parse_args()
    print(args, _add_cmd)

    return 1
