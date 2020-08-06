#!/bin/bash
pip install selenium --user
cd /tmp/
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
curl https://intoli.com/install-google-chrome.sh | bash &> /tmp/chromeinstall.txt
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
google-chrome --version && which google-chrome
