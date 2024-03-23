# Micropython Examples for ESP32 "Cheap Yellow Display"
This is display and touch screen boilerplate to use with Micropython on the ["CYD"](https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display).

# Full instructions

Full instructions to get this working graciously provided by [kf107](https://github.com/kf107) from [thinklayer.com](https://thinklair.com) in a [Medium Article here](https://kf106.medium.com/how-to-use-micropython-on-a-cyd-cheap-yellow-display-e158d5e4a2e7).

A mirror of the instructions in text format in case the article goes missing are located in the repo as medium_instructions.md.

# Quick Instructions at a glance

Flash the CYD with Micropython ESP32 Generic.
I suggest using the most current stable release, not a development release.
[https://micropython.org/download/ESP32_GENERIC/](https://micropython.org/download/ESP32_GENERIC/)

Clone this repo and upload the files to your board using Thonny, rshell or whatever IDE extension that can talk to the board.

Reboot and try it out. Your touch screen may not report the same values, so will need altering.

Libraries from [@rdagger](https://github.com/rdagger):

[https://github.com/rdagger/micropython-ili9341](https://github.com/rdagger/micropython-ili9341)
