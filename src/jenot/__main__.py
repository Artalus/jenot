from typing import Optional, Sequence, NamedTuple
from configargparse import ArgumentParser

import jenot
import jenot.notify as jnotify

class Args(NamedTuple):
    url: str
    token: str
    user: str
    build: str
    zenity: bool
    telegram: bool

def parse_args(argv: Optional[Sequence[str]] = None) -> Args:
    parser = ArgumentParser(default_config_files=['~/.jenotrc', './.jenotrc'])
    parser.add("-j", "--url")
    parser.add("-t", "--token")
    parser.add("-u", "--user")
    parser.add("-z", "--zenity", action='store_true')
    parser.add("-tg", "--telegram", action='store_true')
    parser.add("build")

    return Args(**parser.parse_args(argv).__dict__)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_args(argv)
    result = jenot.run(args.url, args.user, args.token, args.build)
    if args.zenity:
        jnotify.zenity(args.build, bool(result))
    if args.telegram:
        jnotify.telegram(args.build, bool(result))
    exit(result)


if __name__ == "__main__":
    main()
