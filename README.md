  <br>
  <h1 align="center">Raspberry Pi Dashboard with Home Assistant</h1>
  <br>
 <h2 align="center">
<img src="https://github.com/NielsU97/HomeDisplay/blob/main/www/Images/hass_homedisplay.jpg" width="500">
  </br>
</br>  
<h2>	  
<h2> Install Kiosk </h2>
</br>

`SSH` - Connect to your Pi using Secure Shell (Command prompt) with Hostname or IP address
```
ssh username@hostname

ssh username@192.xxx.x.xx
```
Or use PuTTY instead of command prompt. 


`Command 1` - Check and Update our Pi
```
sudo apt-get update -y
```
```
sudo apt-get upgrade -y
```

</br>

`Command 2` - Install minimum GUI components (Used for Chomium)
```
sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox
```

</br>

`Command 3` - Install Chromium Web browser 
```
sudo apt-get install --no-install-recommends chromium-browser
```

</br>

`Command 4` - Edit Openbox config
```
sudo nano /etc/xdg/openbox/autostart
```
Enter the following lines
```
# If you want to use XFCE config tools...

#xfce-mcs-manager &
xset -dpms            # turn off display power management system
xset s noblank        # turn off screen blanking
xset s off            # turn off screen saver

# Remove exit errors from the config files that could trigger a warning

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/'Local State'

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/; s/"exit_type":"[^"]\+"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences

# Run Chromium in kiosk mode
chromium-browser  --noerrdialogs --disable-infobars --enable-features=OverlayScrollbar --kiosk $KIOSK_URL --check-for-update-interval=31536000
```
Save and exit file
</br>

`Command 5` - Setup Openbox environment 
```
sudo nano /etc/xdg/openbox/environment
```
Enter the following line
```
export KIOSK_URL=https://YourHomeAssistant_URL
```
Save and exit file
</br>

`Command 6` - Start the X server on boot. Check if bash_profile exists
```
ls -la ~/.bash_profile
```
If it doesn't exist create it
```
touch ~/.bash_profile
```

</br>

`Command 7` - Edit Bash Profile
```
sudo nano ~/.bash_profile
```
Enter the following line in the file
```
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
```
Save and exit file
</br>

`Command 8` - Check ~/.bash_profile
```
source ~/.bash_profile
```

</br>

`Command 9` - Reboot Pi
```
sudo reboot
```

</br>
<p> Code used from <a href="https://desertbot.io/blog/raspberry-pi-touchscreen-kiosk-setup" target="_blank">Desertbots</a> and 
<a href="https://github.com/MarkWattTech/MarkWattTech-Tutorials/tree/1c9476771c0ee778977c53e3dc3d8a13b47b9ab2/A%20DIY%20Home%20Assistant%20Kiosk" target="_blank">MarkWattTech</a>

</p>

<h2> Extra: Turn off/on the screen using ToF sensor </h2>
<br>
I have added a Time-of-Flight (ToF) sensor to automatically turn the screen on and off. Without this sensor, the screen would remain constantly on, leading to increased power consumption. <a href="https://github.com/NielsU97/HomeDisplay/blob/main/display_motion_react.py" target="_blank">Klik here for the code example</a>.
<br>
</br>

`Command 1` - Create a unit file
```
sudo nano /lib/systemd/system/display_motion_react.service
```

</br>

`Command 2` - Add in the following text (Check your path)
```
[Unit]
Description=My Sample Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/pi/display_motion_react.py

[Install]
WantedBy=multi-user.target
```

</br>

`Command 3` - Enable the unit file which starts the program during the boot sequence
```
sudo systemctl daemon-reload
```
```
sudo systemctl enable display_motion_react.service
```

</br>

`Command 4` - Reboot Pi and your custom service should start on boot
```
sudo reboot
```
