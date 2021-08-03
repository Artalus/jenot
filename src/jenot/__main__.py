from typing import Optional, Sequence, NamedTuple
from configargparse import ArgumentParser
import jenot

class Args(NamedTuple):
    url: str
    token: str
    user: str
    build: str

def parse_args(argv: Optional[Sequence[str]] = None) -> Args:
    parser = ArgumentParser(default_config_files=['~/.jenotrc', './.jenotrc'])
    parser.add("-j", "--url")
    parser.add("-t", "--token")
    parser.add("-u", "--user")
    parser.add("build")

    return Args(**parser.parse_args(argv).__dict__)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_args(argv)
    jenot.run(args.url, args.user, args.token, args.build)


if __name__ == "__main__":
    main()
