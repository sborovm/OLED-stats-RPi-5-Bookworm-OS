# This is changed display stats script that was inspired by Michael Klemens script - https://youtu.be/lRTQ0NsXMuw?si=-ikytmVryK5GhTix and https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/

# This script is for Raspberry Pi5 and Bookworm OS.
# You have to bear in mind that Python have to be run in virtual environment. To do that you have to use this commands. 
# Firstly you have to make an directory where your project will be saved and where all libraries will be saved.
mkdir my_project 
# You can choose directory as you want. I choosed my_project
cd my_project
python3 -m venv venv
# Now you have to activate this virtual environment:
source venv/bin/activate
# Now install all libraries with pip command (LUMA.oled - https://luma-core.readthedocs.io/en/stable/intro.html)
# Save file display_stats_new.py in this directory.
# If you want to run this script on system startup you have to use this:
crontab -e
@reboot /my_project/venv/bin/python3 /my_project/display_stats_new.py

# Once you reboot your raspberry it should show the disply stats

# All this work is a result of many hours with ChatGPT because I am not a python programmer.
