sudo mount /dev/sda1 /media/usb
sudo sed -i 's/\r$//' /etc/init.d/JustAnotherRunItScript.sh
cd /media/usb/
cd PythonProjectForPycharm/
python3 bot.py