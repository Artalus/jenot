from __future__ import annotations
from typing import (
    Optional,
    NamedTuple,
    Sequence,
)

from configargparse import ArgumentParser


class Args(NamedTuple):
    url: str
    token: str
    user: str
    build: Optional[str]
    zenity: bool
    telegram: bool
    pynotifier: bool

    @staticmethod
    def parse(argv: Optional[Sequence[str]] = None, build_required: bool=True) -> Args:
        parser = ArgumentParser(default_config_files=['~/.jenotrc', './.jenotrc'])
        parser.add_argument("-j", "--url", required=True)
        parser.add_argument("-t", "--token", required=True)
        parser.add_argument("-u", "--user", required=True)
        parser.add_argument("-zn", "--zenity", action='store_true')
        parser.add_argument("-tg", "--telegram", action='store_true')
        parser.add_argument("-pn", "--pynotifier", action='store_true')
        # would use 1, but it results in ['...'] instead of '...', so use None
        parser.add_argument("build", nargs=(None if build_required else '?'))

        return Args(**parser.parse_args(argv).__dict__)
