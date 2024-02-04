# Selenium usage

## Installation guide

1. Install python, pip and google chrome
   google chrome:
   `wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - `
   `sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'`
   `sudo apt-get update`
   `sudo apt-get install google-chrome-stable`
   python:
   `sudo apt install python3.8`
   pip:
   `sudo apt-get -y install python3-pip`
2. Install Selenium python library, in case of a server install `pyvirtualdisplay` python library and `xvfb` too
   - `pip3 install selenium`
     `pyvirtualdisplay` and `xvfb` (optional)
   - `sudo apt install -y xvfb` (optional)
   - `pip3 install pyvirtualdisplay` (optional)
3. Get your chrome driver of your version here: https://sites.google.com/chromium.org/driver/downloads?authuser=0 and save it as `chromedriver` in the `./drivers` folder
4. Run the script `python3 seleniumFrogs.py`