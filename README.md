# Photobooth Project:GPIO implementation for buttons and rotary encoder on Pi OS Bookworm
This code allows you to connect hardware buttons and a rotary encoder to the GPIOs of a Raspberry Pi with the latested Raspberry Pi OS Bookwork (Linux 6.6 Kernel) in the Photooboth Project of Andreas Skomski. Support in the Photobooth Project was broken as Linux 6.6 Kernel is not able to handle the GPIO buttons via sysfs anymore.

Preparation:

Copy the following lines to the end of config.txt:

sudo nano /boot/firmware/config.txt

    dtoverlay=rotary-encoder,pin_a=17,pin_b=27,relative_axis=1,steps-per-period=1
    dtoverlay=gpio-key,gpio=22,keycode=28,label=ENTER",gpio_pull=2
    dtoverlay=gpio-key,gpio=21,keycode=20,label="t",gpio_pull=2
    dtoverlay=gpio-key,gpio=20,keycode=46,label="c",gpio_pull=2
    dtoverlay=gpio-key,gpio=26,keycode=25,label="p",gpio_pull=2
    dtoverlay=gpio-key,gpio=5,keycode=22,label="u",gpio_pull=2
    dtoverlay=gpio-key,gpio=16,keycode=31,label="s",gpio_pull=2
    dtoverlay=gpio-key,gpio=11,keycode=50,label="m",gpio_pull=2

Start the script with the command "python3 gpiosupport.py" or set it up as an autostart script (cronjob/service). If it does not work install the required dependency python3-evdev first: sudo apt install python3-evdev.
