# ETV Timer Pi

A countdown timer application to run on a Raspberry Pi built for the escape room company
[Escape The Vault](https://www.escapethevault.com.au/).

## Motivation

My brother started an escape room business and wanted countdown timers in
each of the rooms so participants could see how long they had left to solve
the puzzles.

Timers like this already existed but didn't really fit the requirement
of providing both the participants and the staff the countdown timer as the physical
timer would be inside the room where staff outside could not see it. Also these existing timers
were very expensive.

To solve this I built a Wifi connected Raspberry Pi countdown timer that uses a LED clock
in the rooms for the participants to see and also serves a UI over the local network for
staff to see and also to control the timer.

## About

ETV Timer Pi is built with the python framework Flask, Bootstrap and socketio.

## Hardware

- [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [7 Segment Clock Display](https://www.adafruit.com/product/1264)

## Author

Jeremy Storer <storerjeremy@gmail.com>