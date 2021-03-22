import argparse

from egob import __version__, __author__

HEADER = "\n".join(
    [
        r"  #######   #####    #####   ###### ",
        r' ##   #  ##   ##  ### ###   ##  ##',
        r" ##      ##       ##   ##   ##  ##",
        r" ####    ## ####  ##   ##   #####",
        r" ##      ##   ##  ##   ##   ##  ##",
        r"##   #  ##   ##  ### ###   ##  ##",
        r"#######   #####    #####   ######",
        "                                                    ",
        f" ver. {__version__}     author {__author__}        ",
        "                                                    ",
    ]
)


def get_parser():
    parser = argparse.ArgumentParser(prog="egob")

    subparsers = parser.add_subparsers(dest="command", help="egob sub-commands")
    subparsers.required = True

    subparsers.add_parser("deploy", help="Deploy server")

    return parser


def cli():
    print(HEADER)
    args, _ = get_parser().parse_known_args()

    if args.command == "deploy":
        from egob.app import run_server

        run_server()


if __name__ == "__main__":
    cli()