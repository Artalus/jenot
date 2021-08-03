# JeNot - Jenkins Notifications

<img src="/logo.png" height=200px width=200px>

## What
A tool to monitor status of Jenkins builds and notify you when they are done.

## Why
Jenkins has tons of various plugins and integrations to send notifications anywhere, from emails to teapots. Yet all of these require that the Job contains some `sendNotification(receiver)` code.

Meanwhile, there are cases where only you personally are interested in said notification. Perhaps you are an admin waiting for some build to release the node, so you can reboot it. Or maybe you are an eager tester waiting for someone else's build to finish.

In that case, you have to monitor jenkins jobs from outside. Enter jenot.

## How
By using your username and API token to bang on Jenkins REST API and hope that at some point it responds with `{"finished": true}`. In that case - cue fanfare, [Zenity](https://help.gnome.org/users/zenity/), [telegram-send](https://github.com/rahiel/telegram-send) et. cetera.
