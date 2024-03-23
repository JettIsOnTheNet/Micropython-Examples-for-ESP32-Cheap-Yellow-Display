### These instructions were scraped with links, and quickly formatted to markdown. It is only preserved in case the article goes unavailable. Please reference [the article located here](https://kf106.medium.com/how-to-use-micropython-on-a-cyd-cheap-yellow-display-e158d5e4a2e7).
---------
# Instructions from kf107 from thinklair.com
   A while back I stumbled across Witnessmenow’s Cheap Yellow Display
   repository, and thought that it looked interesting (and cheap at $15 or so
   per device).

   Unfortunately it didn’t cover using Micropython on the device, and I hate
   using C++, so I ended up with two of them sitting on my desk doing
   nothing.

   Today I finally found a repository providing the code to get Micropython
   working on a CYD, but the instructions were rather brief, so I though I’d
   document how I got it to work for anyone else in the same position as me.

   This guide walks you through getting everything set up and working,
   assuming you are using Ubuntu 22.04. If you’re using MacOS or Windows, it
   should help, but you’ll have to dig out the platform specific steps by
   searching the web yourself.

   So, let’s get started.

### Set up your environment

   We want to use a virtual environment so we don’t mess up our Python
   installation on our machine.
```
 mkdir CYD-micropython
 cd CYD-micropython
 mkdir venv
 python -m venv ./venv
 source venv/bin/activate
```
   Then we install the esptool for flashing files to the CYD, and thonnyfor
   uploading files after we’ve flashed the CYD with Micropython.
```
 pip install esptool
 sudo apt-get install thonny
```
### Obtaining the Python driver files

   Clone JettisOnTheNet’s example and drivers for Micropython on the CYD:
```
 git clone https://github.com/JettIsOnTheNet/Micropython-Examples-for-ESP32-Cheap-Yellow-Display
```
### Gathering port information

   You will need to connect your CYD to your PC using a USB-micro cable (but
   don’t do it quite yet). Note that the USB cable has to be a data carrying
   cable — many of these cables are for power only. If the next steps don’t
   work, your first step should be to try a new cable.

   Get a list of current terminal ports:
```
 ls /dev/tty
```
   Then plug the board in, and run the above command again. A new port will
   appear in the list of ports shown. It is probably /dev/ttyUSB0. That’s
   your board port.

   You can now query the board over the USB port. For example:
```
 esptool.py -p /dev/ttyUSB0 flash_id
```
   Remember to replace ttyUSB0with your port number. This commad will return
   information about your board.

### Erasing the flash memory

   Now we need to clear the flash memory, and that involves getting the board
   into flash mode.

   Press the RESET (EN) button (top-left most button behind the board as you
   look at the screen) and the BOOT button (just to the right of the RESET
   button: they’re both labelled on the board) at the same time, then let go
   of the RESET button first and the BOOT button second.

   Hint: with a bit of practice you will learn how to do this by rolling your
   finger across the two buttons from left to right.

   The board won’t boot up into the demo program flashed onto it in the
   factory. Instead, the screen will stay black, but the red LED on the back
   of the board will remain lit to show power is connected.

   Because this is the first time we’re putting Micropython on the CYD, it is
   best to completely erase the flash:
```
 esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```
   This time, after the message Hard resetting via RTS pin the board won’t
   boot up into the demo program, because it’s not there.

### Flashing with Micropython

   Download the Micropython image from
   ```
   https://micropython.org/download/ESP32_GENERIC/
```
   I used the first version I saw, namely v1.22.2 (2024–02–22) .bin, which
   worked.

   Flash it to the board by putting it into flash mode, and running the
   esptool with the following command:
```
 esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20240222-v1.22.2.bin
```
### Running Thonny and uploading the Python scripts

   Thonny is a Micropython IDE that you can use to upload files to your
   board, as an editor, and to test your scripts before trying to run them at
   the board. For now, we’re just going to use it to upload the files we need
   from JettisOnTheNet’s repository, so we don’t see a blank screen anymore.

   At the command line start Thonny:
```
 thonny
```
   The Thonny GUI should appear. The first time you’ll be asked to pick your
   language and settings. I just went with the defaults. Then this screen
   appears:

   First, we will connect the board to Thonny. Select Tools > Options, and
   then the Interpreter tab.

   From the “Which kind of interpreter should Thonny use for running your
   code?” dropdown, select MicroPython (ESP32).

   This changes the view in the Interpreter pane to show you the “Port or
   WebREPL” dropdown, which allows you to select the USB serial port you need
   to use — that’s the one you found out about above, for example USB Serial
   @ /dev/ttyUSB0 or whatever number you found out.

   Then click on the OK button.

   Now we are going to find the files we need to upload. Selected View >
   Files from the menu bar to show the file selection pane. Use the file pane
   to navigate to the Micropython-Examples-for-ESP32-Cheap-Yellow-Display
   folder you cloned from JettisOnTheNet’s github repository

   Double click on boot.py, ili9341.pyand xpt2046.py to open each in its own
   editor pane.

   You can get rid of <untitled> tab by clicking on the x next to it.

   Then we save each of the three files to the CYD:

   Go to each file tab in turn, then select the menu option File > Save as…,
   and select MicroPython device. Enter the correct name for each file (as it
   doesn’t remember it). A second pane will appear in the Files tab, with the
   heading MicroPython device, showing each file as you save it.

   When all three files are copied across, you can hit the RESET button on
   your CYD, and the app will run. It puts a dot on the screen where you tap
   it, and shows the x and y co-ordinates at the bottom of the screen.

   Congratulations — you’ve installed Micropython, and loaded some scripts
   across that run a Python program on your CYD.

### Afterword

   At this point I hit a problem trying to upload new edited files for the
   CYD at this point. The script locks the device, and even re-flashing it
   doesn’t get it out of the locked state.

   It turns out you have to click in the Shell pane and then press Ctrl+C to
   exit the Python program running on the CYD, which puts you into a Python
   REPL and allows you to run Python commands on the device from the
   interpreter dynamically.

   For example, try the following to list the files you loaded on to the
   device:

```
 >>> import os
 >>> os.listdir()
 ['boot.py', 'ili9341.py', 'xpt2046.py']
```