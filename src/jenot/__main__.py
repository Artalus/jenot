import jenot
from jenot.args import Args
import jenot.notify as jnotify


def main() -> None:
    args = Args.parse(build_required=True)
    assert args.build
    result, url = jenot.run(args.url, args.user, args.token, args.build)
    if args.zenity:
        jnotify.zenity(url, result==0)
    if args.telegram:
        jnotify.telegram(url, result==0)
    if args.pynotifier:
        jnotify.pynotifier(url, result==0)
    exit(result)


if __name__ == "__main__":
    main()
