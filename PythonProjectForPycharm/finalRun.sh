SCRIPT_LOCATION="/media/usb/PythonProjectForPycharm/"
$SCRIPT_LOCATION./Berryconda3-2.0.0-Linux-armv7l.sh -b
sudo chmod 777 $SCRIPT_LOCATION
cd $SCRIPT_LOCATION
/home/pi/berryconda3/bin/pip install -r requirements.txt
/home/pi/berryconda3/bin/python3.6 bot.py