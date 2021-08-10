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
        parser.add("-j", "--url")
        parser.add("-t", "--token")
        parser.add("-u", "--user")
        parser.add("-zn", "--zenity", action='store_true')
        parser.add("-tg", "--telegram", action='store_true')
        parser.add("-pn", "--pynotifier", action='store_true')
        # would use 1, but it results in ['...'] instead of '...', so use None
        parser.add("build", nargs=(None if build_required else '?'))

        return Args(**parser.parse_args(argv).__dict__)
