# JeNot - Jenkins Notifications <img src="src/jenot/data/logo.png" height=100px width=100px>

## What
A tool to notify you when Jenkins builds are done.

## Why
Jenkins has tons of various plugins and integrations to send notifications anywhere, from emails to teapots. Yet all of these require that the Job must contain some `sendNotification(receiver)` code.

Meanwhile, there are cases where only you personally are interested in said notification. Perhaps you are an admin waiting for some build to release the node, so you can reboot it. Or maybe you are an eager tester waiting for someone else's build to finish. Especially if your Jenkins is not a CI but simple Automation server.

In that case, you have to monitor Jenkins jobs from outside. Enter jenot.

## How
By using your username and API token to bang on Jenkins REST API and hope that at some point it responds with `{"finished": true}`. In that case - cue fanfare, [Zenity](https://help.gnome.org/users/zenity/), [telegram-send](https://github.com/rahiel/telegram-send) et. cetera.

## Developing
- `git clone`
- `python -m venv venv && . venv/bin/activate`
- `pip install -e .`
- debug in VS Code:
```json
// launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "jenot.qt",
            "type": "python",
            "request": "launch",
            "module": "jenot.qt"
        }
    ]
}
```

## Installing
- `pip install https://github.com/Artalus/jenot/archive/refs/heads/master.zip`
TODO: provide executables from pyinstaller or something
