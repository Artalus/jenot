from typing import cast
import jenot
from jenot.args import Args
import jenot.notify as jnotify


def main() -> None:
    args = Args.parse(build_required=True)
    assert args.build
    result, refined_url = jenot.run_poll(args.url, args.user, args.token, args.build)

    value = result.unwrap()
    if value is None:
        ok = False
    else:
        ok = cast(jenot.PollResult, value).success

    if args.zenity:
        jnotify.zenity(refined_url, result)
    if args.telegram:
        jnotify.telegram(refined_url, result)
    if args.pynotifier:
        jnotify.pynotifier(refined_url, result)

    exit(0 if ok else 1)


if __name__ == "__main__":
    main()
